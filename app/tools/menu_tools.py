from app.database.db import SessionLocal
from app.models.models import MenuItem

def get_menu() -> str:
    """
    Fetch full restaurant menu from database.
    """
    db = SessionLocal()
    items = db.query(MenuItem).all()
    db.close()

    if not items:
        return "Menu is currently unavailable."

    menu_text = []
    current_category = None

    for item in items:
        if item.category != current_category:
            menu_text.append(f"\n{item.category.upper()}:")
            current_category = item.category
        menu_text.append(f"- {item.item_name} (₹{item.price})")

    return "\n".join(menu_text).strip()
