memory_store = {}

def store_memory(user_id, query, answer):

    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append({
        "query": query,
        "answer": answer
    })


def retrieve_memory(user_id, limit=5):

    if user_id not in memory_store:
        return []

    return memory_store[user_id][-limit:]
