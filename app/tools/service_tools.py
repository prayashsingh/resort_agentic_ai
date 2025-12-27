from app.database.db import SessionLocal
from app.models.models import RoomServiceRequest

def create_service_request(room: str, request_type: str) -> str:
    db = SessionLocal()

    request = RoomServiceRequest(
        room_number=room,
        request_type=request_type,
        status="Pending"
    )

    db.add(request)
    db.commit()
    db.close()

    return "Your room service request has been registered successfully."
