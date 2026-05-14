from utils.llm import call_llm


def critic_agent(question, answer, context):

    prompt = f"""
    You are a strict AI Critic.

    Evaluate:
    - hallucination risk
    - grounding quality
    - factual correctness
    - completeness
    - reasoning quality

    Question:
    {question}

    Context:
    {context}

    Proposed Answer:
    {answer}

    Return:
    APPROVED or REJECTED
    with explanation.
    """

    return call_llm(prompt)