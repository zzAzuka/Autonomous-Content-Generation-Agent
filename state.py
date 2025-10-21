from typing import TypedDict, NotRequired

class AgentState(TypedDict):
    user_query: str
    user_topic: str
    research_content: str
    outline_content: str
    outline_approval: NotRequired[bool]
    human_outline_content: NotRequired[str]
    draft_content: str
    draft_approval: NotRequired[bool]
    human_draft_content: str
    final_content: str
