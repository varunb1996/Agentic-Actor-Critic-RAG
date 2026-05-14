from rank_bm25 import BM25Okapi

bm25_documents = []
bm25 = None


def initialize_bm25(chunks):

    global bm25
    global bm25_documents

    bm25_documents = chunks

    tokenized_docs = [
        doc.split()
        for doc in bm25_documents
    ]

    if len(tokenized_docs) == 0:
        print("No BM25 documents found.")
        return

    bm25 = BM25Okapi(tokenized_docs)

    print(f"BM25 initialized with {len(chunks)} chunks")