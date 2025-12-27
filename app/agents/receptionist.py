import json
from app.tools.room_tools import get_available_rooms

# Load static info once
with open("app/config/static_info.json", "r") as f:
    STATIC_INFO = json.load(f)

def handle(message: str) -> str:
    msg = message.lower().strip().strip('"')

    # -----------------------------
    # STATIC FAQ HANDLING
    # -----------------------------
    if "check-in" in msg or "check in" in msg:
        return STATIC_INFO["check_in_time"]

    if "check-out" in msg or "check out" in msg:
        return STATIC_INFO["check_out_time"]

    for facility in ["gym", "spa", "swimming pool", "wifi", "parking"]:
        if facility in msg:
            return STATIC_INFO[facility]

    # -----------------------------
    # ROOM AVAILABILITY (DYNAMIC)
    # -----------------------------
    if "room" in msg and ("available" in msg or "availability" in msg):
        if "deluxe" in msg:
            return get_available_rooms("Deluxe")
        if "suite" in msg:
            return get_available_rooms("Suite")
        return get_available_rooms()

    # -----------------------------
    # FALLBACK
    # -----------------------------
    return (
        "I can help with check-in/check-out times, resort facilities "
        "like gym or spa, or room availability. Please ask!"
    )
