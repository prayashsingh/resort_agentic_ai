from app.database.db import SessionLocal
from app.models.models import MenuItem, Order

def calculate_total(items: list[str], quantities: list[int]) -> float:
    db = SessionLocal()
    total = 0.0

    for item, qty in zip(items, quantities):
        menu_item = db.query(MenuItem).filter(
            MenuItem.item_name.ilike(item)
        ).first()

        if menu_item:
            total += menu_item.price * qty

    db.close()
    return total


def save_order(room: str, items: list[str], quantities: list[int], total: float):
    db = SessionLocal()

    order = Order(
        room_number=room,
        ordered_items=", ".join(items),
        quantities=", ".join(str(q) for q in quantities),
        total_amount=total,
        status="Placed"
    )

    db.add(order)
    db.commit()
    db.close()
