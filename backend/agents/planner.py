from utils.llm import call_llm


def planner_agent(query):

    prompt = f"""
    You are an autonomous planning agent.

    Break the task into:
    - retrieval tasks
    - reasoning tasks
    - web search tasks
    - memory tasks
    - tool calls

    Query:
    {query}
    """

    return call_llm(prompt)