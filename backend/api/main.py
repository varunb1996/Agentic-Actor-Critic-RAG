from fastapi import FastAPI
from pydantic import BaseModel

from agents.graph import run_system

app = FastAPI()


class Query(BaseModel):
    question: str


@app.post("/chat")

def chat(query: Query):

    result = run_system(query.question)

    return result
