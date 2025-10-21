from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()

CHAT_MODEL = "gemini-2.5-flash-preview-05-20"

LLM = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    temperature=0.7,
    google_api_key=os.getenv("GEM_API_KEY")
)

JUDGE_LLM = ChatGoogleGenerativeAI(
    model=CHAT_MODEL,
    temperature=0.7,
    google_api_key=os.getenv("GEM_API_KEY")
)

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general",
    tavily_api_key = os.getenv("TAV_API_KEY")
    )