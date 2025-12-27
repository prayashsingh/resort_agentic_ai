from app.tools.service_tools import create_service_request

# Session-level context for multi-turn flows
SERVICE_CONTEXT = {}

AMENITIES = ["toiletries", "toothpaste", "pillow", "blanket", "blankets"]

def handle(message: str, room: str, session_id: str) -> str:
    msg = message.lower().strip().strip('"')

    # Initialize context
    if session_id not in SERVICE_CONTEXT:
        SERVICE_CONTEXT[session_id] = {
            "request_type": None,
            "quantity": None,
            "awaiting_confirmation": False
        }

    ctx = SERVICE_CONTEXT[session_id]

    # ---------- CLEANING ----------
    if "clean" in msg:
        create_service_request(room, "Room Cleaning")
        del SERVICE_CONTEXT[session_id]
        return "Room cleaning request has been created."

    # ---------- LAUNDRY ----------
    if "laundry" in msg:
        create_service_request(room, "Laundry Service")
        del SERVICE_CONTEXT[session_id]
        return "Laundry service request has been created."

    # ---------- AMENITIES ----------
    for amenity in AMENITIES:
        if amenity in msg:
            ctx["request_type"] = f"Extra {amenity.capitalize()}"
            return f"How many {amenity}s do you need?"

    # ---------- QUANTITY ----------
    if msg.isdigit() and ctx["request_type"]:
        ctx["quantity"] = int(msg)
        ctx["awaiting_confirmation"] = True
        return (
            f"Please confirm your request for "
            f"{ctx['quantity']} {ctx['request_type']} (yes/no)."
        )

    # ---------- CONFIRMATION ----------
    if msg in ["yes", "confirm"] and ctx["awaiting_confirmation"]:
        create_service_request(
            room,
            f"{ctx['request_type']} x{ctx['quantity']}"
        )
        del SERVICE_CONTEXT[session_id]
        return "Your request has been confirmed and sent to housekeeping."

    if msg == "no":
        del SERVICE_CONTEXT[session_id]
        return "Request cancelled. Let me know if you need anything else."

    # ---------- FALLBACK ----------
    return (
        "I can help with room cleaning, laundry service, or extra "
        "amenities like pillows, blankets, toothpaste, or toiletries."
    )
