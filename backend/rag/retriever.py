from sentence_transformers import SentenceTransformer
import chromadb

from rag.bm25_store import bm25_search

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    "advanced_rag"
)

def vector_search(query, top_k=3):

    embedding = embedding_model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results["documents"][0]

def hybrid_search(query):

    vector_results = vector_search(query)

    bm25_results = bm25_search(query)

    combined = list(
        set(vector_results + bm25_results)
    )

    return combined