from langchain_core.prompts import ChatPromptTemplate
from state import AgentState
from config import LLM

def draft(state: AgentState):
    """The LLM call that is used to draft a fully-fledged article user topic and the outline to be followed."""

    print("AT DRAFT NODE!")

    try:
        if state["human_draft_content"] != "":
            prompt = ChatPromptTemplate.from_messages([
                ("system",
                """You are an intelligent article write who drafts detailed and rich articles.
                    Using the results from your knowledge, the topic and the outline to follow, and the feedback from the user craft a detailed article."""),
                ("user", """Give me a detailed and researched article on {user_topic}
                            Outline to follow: {outline_content}
                            User Feedback: {human_draft_content}""")
            ])

            format_prompt = prompt.format_messages(user_topic=state["user_topic"], outline_content=state["outline_content"], human_draft_content=state["human_draft_content"])
            draft_response = LLM.invoke(format_prompt)
            #print(f"Research Node Response: {research_response.content}")

            state["draft_content"] = draft_response.content
            file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\draft.txt","w")
            file.write(state["draft_content"])
            file.close()

            return state
        
        else:
            prompt = ChatPromptTemplate.from_messages([
            ("system",
            """You are an intelligent article write who drafts detailed and rich articles.
                Using the results from your knowledge, the topic and the outline to follow, craft a detailed article."""),
            ("user", """Give me a detailed and researched article on {user_topic}
                        Outline to follow: {outline_content}""")])

            format_prompt = prompt.format_messages(user_topic=state["user_topic"], outline_content=state["outline_content"])
            draft_response = LLM.invoke(format_prompt)
            #print(f"Research Node Response: {research_response.content}")

            state["draft_content"] = draft_response.content
            file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\draft.txt","w")
            file.write(state["draft_content"])
            file.close()

        return state
    except Exception as e:
        print("Error:",e)
