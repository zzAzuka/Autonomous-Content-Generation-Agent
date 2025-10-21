from langchain_core.prompts import ChatPromptTemplate
from state import AgentState
from config import LLM

"""The LLM call that is used to take in a research content, outline, article draft and evaluate them."""

print("AT EVALUATE NODE!")

try:
    prompt = ChatPromptTemplate.from_messages([
        ("system",
        """You are an intelligent and professional critic who critics reserach content, outlines and final drafts of articles.
            When provided with the content to critic and score, use the following guidelines.
            
            Guidelines:
            - You will have to act as a critic and judge the given topics
            - For the reserach content, Evaluate depth, relevance and source credibility.
            - For the outline content, Assess the logical flow, completeness and clarity
            - For the draft content, Analyze the writing quality, Coherence and Engagement
               
           Provide scores out of 10, for each research, outline and draft content. Give a one-liner on why the score was given."""
            ),
        ("user", """Research Content: {research_content}
                    Outline Content: {outline_content}
                    Draft Content: {draft_content}""")
        ])

    research_file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\research.txt","r")
    outline_file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\outline.txt","r")
    draft_file = open("C:\\Sibi\\CrayonD\\Task Implementations\\sibi-week-3\\content_creation_agent\\draft.txt","r")

    research_content = research_file.read()
    outline_content = outline_file.read()
    draft_content = draft_file.read()

    format_prompt = prompt.format_messages(research_content=research_content, outline_content=outline_content, draft_content=draft_content)
    evaluation_response = LLM.invoke(format_prompt)
    print(f"Evaluation: {evaluation_response.content}")
        

except Exception as e:
        print("Error:",e)
