# =================================================
# GLOBAL IN-MEMORY SESSION STORAGE
# =================================================

from typing import Dict, List

# Structure:
# SESSION_MEMORY = {
#   session_id: {
#       "messages": [...],
#       "context": {...}
#   }
# }

SESSION_MEMORY: Dict[str, Dict] = {}


def get_session_history(session_id: str) -> List[Dict[str, str]]:
    """
    Returns chat history (messages) for a session.
    Used by chat API.
    """
    if session_id not in SESSION_MEMORY:
        SESSION_MEMORY[session_id] = {
            "messages": [],
            "context": {}
        }
    return SESSION_MEMORY[session_id]["messages"]


def get_session_context(session_id: str) -> Dict:
    """
    Returns mutable context for multi-turn agent workflows
    (restaurant, room service).
    """
    if session_id not in SESSION_MEMORY:
        SESSION_MEMORY[session_id] = {
            "messages": [],
            "context": {}
        }
    return SESSION_MEMORY[session_id]["context"]
