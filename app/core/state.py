from typing import TypedDict, List, Dict

class AgentState(TypedDict):
    session_id: str
    room_number: str
    user_message: str
    intent: str
    messages: List[Dict[str, str]]
