from rag.bm25_store import bm25, bm25_documents


def hybrid_retrieve(query, top_k=3):

    if bm25 is None:
        return ["BM25 not initialized"]

    tokenized_query = query.split()

    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(
        zip(bm25_documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked[:top_k]]