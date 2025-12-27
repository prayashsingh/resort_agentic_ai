from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.db import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    room_number = Column(String, unique=True, nullable=False)
    room_type = Column(String, nullable=False)
    status = Column(String, nullable=False)


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String)        # ✅ MUST EXIST
    price = Column(Float, nullable=False)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    room_number = Column(String, nullable=False)
    ordered_items = Column(String, nullable=False)
    quantities = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="Placed")
    timestamp = Column(DateTime, default=datetime.utcnow)


class RoomServiceRequest(Base):
    __tablename__ = "room_service_requests"

    id = Column(Integer, primary_key=True)
    room_number = Column(String, nullable=False)
    request_type = Column(String, nullable=False)
    status = Column(String, default="Pending")
    timestamp = Column(DateTime, default=datetime.utcnow)
