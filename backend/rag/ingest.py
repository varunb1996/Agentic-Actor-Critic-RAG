from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from sentence_transformers import (
    SentenceTransformer
)

import chromadb

from rag.bm25_store import initialize_bm25

from rag.graphrag import (
    build_graph_from_chunks
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    "advanced_rag"
)


def ingest_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    chunk_texts = []

    for i, chunk in enumerate(chunks):

        text = chunk.page_content

        chunk_texts.append(text)

        embedding = embedding_model.encode(
            text
        ).tolist()

        collection.add(
            ids=[f"{pdf_path}_{i}"],
            embeddings=[embedding],
            documents=[text],
            metadatas=[
                {
                    "source": pdf_path
                }
            ]
        )

    initialize_bm25(chunk_texts)

    build_graph_from_chunks(chunk_texts)

    print(f"Ingestion complete for: {pdf_path}")