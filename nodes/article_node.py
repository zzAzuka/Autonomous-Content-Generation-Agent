from langchain_core.prompts import ChatPromptTemplate
from state import AgentState
from config import LLM

def article(state: AgentState):
    """The LLM call that is used to take in a user topic, article draft and create a final article."""

    print("AT FINAL ARTICLE NODE!")

    try:
        prompt = ChatPromptTemplate.from_messages([
            ("system",
            """You are an intelligent article writer agent.
                Using the results from your knowledge, the rough draft and User Topic make a very well structured
                and professional article."""),
            ("user", "The topic is {user_topic} and the rought draft is: {draft_content}")
        ])

        format_prompt = prompt.format_messages(user_topic=state["user_topic"], draft_content=state["draft_content"])
        final_response = LLM.invoke(format_prompt)
        #print(f"Research Node Response: {research_response.content}")

        state["final_content"] = final_response.content
        state["human_outline_content"] = ""

        print("The Article Generated:")
        print(state["final_content"])
        
        return state
    except Exception as e:
        print("Error:",e)
