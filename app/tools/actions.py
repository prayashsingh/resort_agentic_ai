from app.database.db import SessionLocal
from app.models.models import Order, RoomServiceRequest

def create_food_order(room_number: str, items: list):
    db = SessionLocal()
    order = Order(
        room_number=room_number,
        items=", ".join(items),
        total_amount=0  # calculated elsewhere
    )
    db.add(order)
    db.commit()
    db.close()
    return "Food order placed successfully."

def create_room_service_request(room_number: str, request_type: str):
    db = SessionLocal()
    req = RoomServiceRequest(
        room_number=room_number,
        request_type=request_type
    )
    db.add(req)
    db.commit()
    db.close()
    return "Room service request created."
