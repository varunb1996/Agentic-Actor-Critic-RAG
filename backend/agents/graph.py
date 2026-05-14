from agents.actor import actor_agent
from agents.critic import critic_agent
from agents.planner import planner_agent
from agents.memory_agent import retrieve_memory, store_memory
from agents.web_agent import web_search

from rag.hybrid import hybrid_retrieve
from rag.graphrag import graph_expand


bm25_documents = []


def run_system(query, user_id="default"):

    plan = planner_agent(query)

    memory = retrieve_memory(user_id)

    retrieval = hybrid_retrieve(
        query,
        bm25_documents,
    )

    graph_context = graph_expand(query)

    web_results = web_search(query)

    full_context = (
        str(retrieval)
        + "\n"
        + str(graph_context)
        + "\n"
        + str(web_results)
    )

    answer = actor_agent(
        query,
        full_context,
        memory,
    )

    review = critic_agent(
        query,
        answer,
        full_context,
    )

    if "REJECTED" in review:

        answer = actor_agent(
            query,
            full_context + "\nCritic Feedback:\n" + review,
            memory,
        )

    store_memory(user_id, query, answer)

    return {
        "plan": plan,
        "answer": answer,
        "review": review,
    }