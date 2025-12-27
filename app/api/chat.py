from fastapi import APIRouter, Query
from app.core.memory import get_session_history
from app.core.graph import agent_graph
from app.core.state import AgentState   # ✅ REQUIRED

router = APIRouter()

@router.post("/chat")
def chat(
    session_id: str = Query(...),
    room_number: str = Query(...),
    message: str = Query(...)
):
    history = get_session_history(session_id)
    history.append({"role": "user", "content": message})

    state: AgentState = {   # ✅ THIS is what fixes Pylance
        "session_id": session_id,
        "room_number": room_number,
        "user_message": message,
        "intent": "",
        "messages": history
    }

    result = agent_graph.invoke(state)
    reply = result["messages"][-1]["content"]

    return {"reply": reply}
