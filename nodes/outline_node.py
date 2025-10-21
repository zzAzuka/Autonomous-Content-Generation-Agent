from langchain_core.prompts import ChatPromptTemplate
from state import AgentState
from config import LLM

def outline(state: AgentState):
    """The Second LLM call that is used to take in the research content, and provide a strcutured artile outline."""
    
    print("AT OUTLINE NODE!")

    try:
        if state["human_outline_content"] != "":
            prompt = ChatPromptTemplate.from_messages([
            ("system",
            """You are an intelligent artile outline generator who create clear, concice, relevant article outlines from research material.
                Using the results from your knowledge and the feedback from the user you have to give meaningful, well-structured article outline.
                
                Guidelines:
                - Make is comprehensive and professional
                - Implement the user's feedback
                - Make the article outline by covering all the topics and content provided.
                - Structure it with different headings and sub-headings.
                - Try to avoid irrelevant, and extra information and stick to the topic
                - Don't invent new details and maximize the using of the provided content.
                - Include an introduction, necessary headings and sub-headings and a conclusion."""),
            ("user", 
            """Give me a detailed article outline on the topic {user_topic} and the following context.
                Context: {research_content}
                User Feedback: {human_outline_content}""")
            ])
            format_prompt = prompt.format_messages(user_topic=state["user_topic"], research_content = state["research_content"], human_outline_content = state["human_outline_content"])
            outline_response = LLM.invoke(format_prompt)
            #print(f"Outline Node Response: {outline_response.content}")

            state["outline_content"] = outline_response.content

            file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\outline.txt","w")
            file.write(state["outline_content"])
            file.close()

            return state
        
        else:
            prompt = ChatPromptTemplate.from_messages([
                ("system",
                """You are an intelligent artile outline generator who create clear, concice, relevant article outlines from research material.
                Using the results from your knowledge and the feedback from the user you have to give meaningful, well-structured article outline.
                
                Guidelines:
                - Make is comprehensive and professional
                - Make the article outline by covering all the topics and content provided.
                - Try to avoid irrelevant, and extra information and stick to the topic
                - Structure it with different headings and sub-headings.
                - Don't invent new details and maximize the using of the provided content.
                - Include an introduction, necessary headings and sub-headings and a conclusion."""),
                ("user", 
                """Give me a proper article outline on the topic {user_topic} and the following context.
                    Context: {research_content}""")
            ])
            
            format_prompt = prompt.format_messages(user_topic=state["user_topic"], research_content = state["research_content"])
            outline_response = LLM.invoke(format_prompt)
            #print(f"Outline Node Response: {outline_response.content}")

            state["outline_content"] = outline_response.content

            file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\outline.txt","w")
            file.write(state["outline_content"])
            file.close()
            
            return state
    except Exception as e:
        print("Error:",e)
