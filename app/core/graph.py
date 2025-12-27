from langgraph.graph import StateGraph, END
from app.core.state import AgentState
from app.core.intent_router import detect_intent
from app.agents.receptionist import handle as receptionist_handle
from app.agents.restaurant import handle as restaurant_handle
from app.agents.room_service import handle as room_service_handle

# =====================================================
# NODE DEFINITIONS
# =====================================================

def intent_node(state: AgentState):
    intent = detect_intent(
        state["user_message"],
        state["session_id"]
    )
    state["intent"] = intent
    return state



def receptionist_node(state: AgentState):
    """
    Handles receptionist-related queries.
    """
    reply = receptionist_handle(state["user_message"])
    state["messages"].append(
        {"role": "assistant", "content": reply}
    )
    return state


def restaurant_node(state: AgentState):
    """
    Handles restaurant ordering workflow.
    """
    reply = restaurant_handle(
        state["user_message"],
        state["room_number"],
        state["session_id"]
    )
    state["messages"].append(
        {"role": "assistant", "content": reply}
    )
    return state


def room_service_node(state: AgentState):
    """
    Handles room service requests.
    """
    reply = room_service_handle(
        state["user_message"],
        state["room_number"],
        state["session_id"]
    )
    state["messages"].append(
        {"role": "assistant", "content": reply}
    )
    return state


# =====================================================
# GRAPH CONSTRUCTION
# =====================================================

graph = StateGraph(AgentState)

# ---- Add Nodes ----
graph.add_node("intent", intent_node)
graph.add_node("receptionist", receptionist_node)
graph.add_node("restaurant", restaurant_node)
graph.add_node("room_service", room_service_node)

# ---- Entry Point ----
graph.set_entry_point("intent")

# ---- Conditional Routing ----
graph.add_conditional_edges(
    "intent",
    lambda state: state.get("intent", "receptionist"),
    {
        "receptionist": "receptionist",
        "restaurant": "restaurant",
        "room_service": "room_service",
    }
)

# ---- Termination ----
graph.add_edge("receptionist", END)
graph.add_edge("restaurant", END)
graph.add_edge("room_service", END)

# ---- Compile Graph ----
agent_graph = graph.compile()
