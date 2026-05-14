import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

CHROMA_DB_PATH = "./chroma_db"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

LLM_MODEL = "openai/gpt-oss-120b:free"
