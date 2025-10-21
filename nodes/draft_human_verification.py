from state import AgentState
from config import LLM

def draft_human(state: AgentState):
    """The LLM call that is used to get approval from the user about a generated draft"""

    print("AT HUMAN VERIFICATION NODE FOR DRAFT!")

    try:
        generated_draft = state["draft_content"]
        print("The Outline Generated:", generated_draft)

        is_approved = input("Are you satisfied with the draft generated? Type [YES] or [NO]: ")

        if is_approved=="YES":
            state["draft_approval"] = True
            return state
        elif is_approved=="NO":
            state["draft_approval"] = False
            return state
    except Exception as e:
        print("Error:",e)