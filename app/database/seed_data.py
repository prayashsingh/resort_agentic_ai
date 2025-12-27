from app.database.db import engine, SessionLocal, Base
from app.models.models import Room

def seed_rooms():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    db.query(Room).delete()

    rooms = [
        Room(room_number="101", room_type="Deluxe", status="Available"),
        Room(room_number="102", room_type="Deluxe", status="Booked"),
        Room(room_number="201", room_type="Suite", status="Available"),
        Room(room_number="202", room_type="Suite", status="Maintenance")
    ]

    db.add_all(rooms)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_rooms()
