from tavily import TavilyClient
from utils.config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):

    try:

        response = client.search(query=query)

        return response

    except Exception as e:

        return f"Web search error: {e}"
