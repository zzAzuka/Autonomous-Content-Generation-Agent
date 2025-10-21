from state import AgentState

def draft_feedback(state: AgentState):
    """The LLM call that is used to take in the user feedback about a generated draft"""

    print("AT HUMAN FEEDBACK INPUT NODE FOR DRAFT!")

    try:
        #print(state["outline_content"])
        feedback = input("How do you want to improve this outline structure?: ")
        state["human_draft_content"] = feedback
        
        return state
    except Exception as e:
        print("Error:",e)

