from langgraph.graph import StateGraph, END
from state import AgentState
from nodes.research_node import research
from nodes.outline_node import outline
from nodes.outline_human_verification import outline_human
from nodes.outline_feedback_node import outline_feedback
from nodes.draft_node import draft
from nodes.draft_human_verification import draft_human
from nodes.draft_feedback_node import draft_feedback
from nodes.article_node import article

def route_outline_approval(state: AgentState) -> str:
    return "draft_node" if state.get("outline_approval", False) else "outline_feedback_node"

def route_draft_approval(state: AgentState) -> str:
    return "article_node" if state.get("draft_approval", False) else "draft_feedback_node"

def build_workflow():
    workflow = StateGraph(AgentState)
    workflow.add_node("research_node", research)
    workflow.add_node("outline_node", outline)
    workflow.add_node("outline_human_verification", outline_human)
    workflow.add_node("outline_feedback_node", outline_feedback)
    workflow.add_node("draft_node", draft)
    workflow.add_node("draft_human_verification", draft_human)
    workflow.add_node("draft_feedback_node", draft_feedback)
    workflow.add_node("article_node", article)

    workflow.set_entry_point("research_node")

    workflow.add_edge("research_node", "outline_node")
    workflow.add_edge("outline_node", "outline_human_verification")
    workflow.add_conditional_edges("outline_human_verification", route_outline_approval,
        {
            "draft_node": "draft_node",
            "outline_feedback_node": "outline_feedback_node"
        }
    )
    workflow.add_edge("outline_feedback_node", "outline_node")
    workflow.add_edge("draft_node", "draft_human_verification")
    workflow.add_conditional_edges("draft_human_verification", route_draft_approval,
        {
            "article_node": "article_node",
            "draft_feedback_node": "draft_feedback_node"
        }
    )
    workflow.add_edge("draft_feedback_node", "draft_node")
    workflow.add_edge("article_node", END)

    return workflow.compile()

try:
    user_query = input("Enter the topic of the artice that you want to be generated: ")
    chain = build_workflow()
    result = chain.invoke({"user_topic" : user_query})
except Exception as e:
    print("Error:", e)
#print("The researched content:", state['research_content'])
#print("The outline content:", state['outline_content'])