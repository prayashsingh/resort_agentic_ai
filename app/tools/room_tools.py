from app.database.db import SessionLocal
from app.models.models import Room

def get_available_rooms(room_type: str | None = None) -> str:
    db = SessionLocal()

    query = db.query(Room).filter(Room.status == "Available")

    if room_type:
        query = query.filter(Room.room_type.ilike(f"%{room_type}%"))

    rooms = query.all()
    db.close()

    if not rooms:
        return "Currently, no rooms are available."

    room_list = ", ".join(room.room_number for room in rooms)
    return f"Available rooms: {room_list}"
