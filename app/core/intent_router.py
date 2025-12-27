from app.core.llm import call_llm
from app.database.db import SessionLocal
from app.models.models import MenuItem
from app.core.memory import get_session_context

def detect_intent(message: str) -> str:
    msg = message.lower().strip().strip('"')

 # -----------------------------------------
    # 0️⃣ RESPECT ACTIVE RESTAURANT FLOW
    # -----------------------------------------
    ctx = get_session_context(session_id)
    if ctx.get("awaiting_quantity") or ctx.get("awaiting_confirmation"):
        return "restaurant"
    # -----------------------------------------
    # 1. DATABASE-DRIVEN MENU MATCH (FAST PATH)
    # -----------------------------------------
    db = SessionLocal()
    menu_items = db.query(MenuItem.item_name).all()
    db.close()

    for (item_name,) in menu_items:
        item = item_name.lower()
        if item in msg or msg in item:
            return "restaurant"

    # -----------------------------------------
    # 2. KEYWORD FALLBACK
    # -----------------------------------------
    if any(word in msg for word in ["menu", "order", "food", "eat"]):
        return "restaurant"

    if any(word in msg for word in ["clean", "laundry", "pillow", "blanket", "toothpaste", "toiletries"]):
        return "room_service"

    # -----------------------------------------
    # 3. LLM AS LAST RESORT
    # -----------------------------------------
    try:
        messages = [
            {
                "role": "system",
                "content": (
                    "Classify the user message into one of:\n"
                    "receptionist, restaurant, room_service.\n"
                    "Return only the intent name."
                )
            },
            {"role": "user", "content": msg}
        ]

        response = call_llm(messages)
        intent = response.choices[0].message.content.strip().lower()

        if intent in ["receptionist", "restaurant", "room_service"]:
            return intent

    except Exception as e:
        print("⚠️ Intent detection failed:", e)

    return "receptionist"
