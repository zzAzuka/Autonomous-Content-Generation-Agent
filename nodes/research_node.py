from langchain_core.prompts import ChatPromptTemplate
from state import AgentState
from config import LLM, tavily_search_tool


def research(state: AgentState):
    """The First LLM call that is used to take in a user topic, research about it and gather information on it."""

    try:
        search_results = tavily_search_tool.invoke(state["user_topic"])
        #print(search_results)
    except Exception as e:
        print("Error:", e)

    print("AT RESEARCH NODE!")

    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system",
            """You are an expert research assistant who researches about any given topic and provides accurate, professional, organised information. 
                Using the following web search content provided, you have to gather the most relevant information about the topic following the guidelines.
                
                Guidelines:
                - Try to prioritize credible sources
                - Make it professional such that it acts as the root source to write an article.
                - Focus of the key aspects of the topic"""),
            ("user", "Give me a detailed and researched information on {user_topic}"
            "          Search Results: {search_results}")
        ])

        format_prompt = prompt.format_messages(user_topic=state["user_topic"], search_results=str(search_results))
        research_response = LLM.invoke(format_prompt)

        state["research_content"] = research_response.content
        state["human_outline_content"] = ""
        state["human_draft_content"] = ""

        file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\research.txt","w")
        file.write(state["research_content"])
        file.close()
    except Exception as e:
        print("Error:", e)

    return state
