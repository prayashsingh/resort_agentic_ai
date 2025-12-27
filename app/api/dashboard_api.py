from fastapi import APIRouter
from app.database.db import SessionLocal
from app.models.models import Order, RoomServiceRequest

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

# ------------------ RESTAURANT ORDER STATUS ------------------
@router.post("/update-order-status")
def update_order_status(order_id: int, status: str):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        db.close()
        return {"error": "Order not found"}

    order.status = status
    db.commit()
    db.close()
    return {"message": "Order status updated"}

# ------------------ ROOM SERVICE STATUS ------------------
@router.post("/update-service-status")
def update_service_status(request_id: int, status: str):
    db = SessionLocal()
    request = db.query(RoomServiceRequest).filter(
        RoomServiceRequest.id == request_id
    ).first()

    if not request:
        db.close()
        return {"error": "Request not found"}

    request.status = status
    db.commit()
    db.close()
    return {"message": "Service status updated"}
