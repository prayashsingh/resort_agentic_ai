from app.database.db import SessionLocal
from app.models.models import MenuItem, Order
from app.tools.menu_tools import get_menu
from app.core.memory import get_session_context

# =================================================
# RESTAURANT AGENT (FINAL COMBINED VERSION)
# =================================================

def handle(message: str, room_number: str, session_id: str) -> str:
    msg = message.lower().strip().strip('"')

    # -----------------------------------------
    # Load / initialize session context
    # -----------------------------------------
    ctx = get_session_context(session_id)

    ctx.setdefault("selected_item", None)
    ctx.setdefault("awaiting_quantity", False)
    ctx.setdefault("awaiting_confirmation", False)
    ctx.setdefault("quantity", None)

    # -----------------------------------------
    # SHOW MENU
    # -----------------------------------------
    if "menu" in msg:
        return get_menu()

    # -----------------------------------------
    # FETCH MENU ITEMS FROM DATABASE
    # -----------------------------------------
    db = SessionLocal()
    menu_items = db.query(MenuItem).all()
    db.close()

    # -----------------------------------------
    # 1️⃣ DIRECT ITEM MATCH (e.g. "salad", "masala dosa")
    # -----------------------------------------
    for item in menu_items:
        item_name = item.item_name.lower()

        if item_name in msg or msg in item_name:
            ctx["selected_item"] = item
            ctx["awaiting_quantity"] = True
            ctx["awaiting_confirmation"] = False
            return f"How many plates of {item.item_name}?"

    # -----------------------------------------
    # 2️⃣ QUANTITY HANDLING
    # -----------------------------------------
    if ctx["awaiting_quantity"]:
        if msg.isdigit():
            ctx["quantity"] = int(msg)
            ctx["awaiting_quantity"] = False
            ctx["awaiting_confirmation"] = True

            return (
                f"Please confirm your order of "
                f"{ctx['quantity']} plate(s) of {ctx['selected_item'].item_name} (yes/no)."
            )
        else:
            return "Please enter a valid number for quantity."

    # -----------------------------------------
    # 3️⃣ CONFIRMATION HANDLING
    # -----------------------------------------
    if ctx["awaiting_confirmation"]:
        if msg in ["yes", "y", "confirm"]:
            item = ctx["selected_item"]
            qty = ctx["quantity"]
            total = item.price * qty

            # Save order to database
            db = SessionLocal()
            order = Order(
                room_number=room_number,
                ordered_items=item.item_name,
                quantities=str(qty),
                total_amount=total,
                status="Placed"
            )
            db.add(order)
            db.commit()
            db.close()

            # Clear session context
            ctx.clear()

            return f"✅ Order placed successfully! Total bill ₹{total}"

        elif msg in ["no", "n", "cancel"]:
            ctx.clear()
            return "❌ Order cancelled. Let me know if you'd like something else."

        else:
            return "Please reply with yes or no."

    # -----------------------------------------
    # FALLBACK
    # -----------------------------------------
    return (
        "🍽 You can order food by typing the item name "
        "(e.g., 'salad', 'masala dosa', 'pasta') "
        "or type 'menu' to see available dishes."
    )
