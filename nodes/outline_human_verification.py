from state import AgentState

def outline_human(state: AgentState):
    """The LLM call that is used to get approval from the user about a generated outline"""

    print("AT HUMAN VERIFICATION NODE FOR OUTLINE!")

    try:
        generated_outline = state["outline_content"]
        print("The Outline Generated:", generated_outline)

        is_approved = input("Are you satisfied with the outline generated? Type [YES] or [NO]: ")

        if is_approved=="YES":
            state["outline_approval"] = True
            return state
        elif is_approved=="NO":
            state["outline_approval"] = False
            return state
    except Exception as e:
        print("Error:",e)