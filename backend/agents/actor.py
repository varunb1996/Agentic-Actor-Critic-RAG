from utils.llm import call_llm


def actor_agent(question, context, memory):

    prompt = f"""
    You are the Actor Agent.

    Memory:
    {memory}

    Context:
    {context}

    User Question:
    {question}

    Generate the best grounded response.
    """

    return call_llm(prompt)