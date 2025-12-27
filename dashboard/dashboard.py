import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import requests

BACKEND_URL = "http://localhost:8000"
engine = create_engine("sqlite:///resort.db")

st.set_page_config(page_title="Resort Operations Dashboard", layout="wide")
st.title("🏨 Resort Operations Dashboard")

# ============================================================
# 🍽 RESTAURANT REQUESTS
# ============================================================
st.header("🍽 Restaurant Requests")

orders = pd.read_sql("SELECT * FROM orders", engine)

if orders.empty:
    st.info("No restaurant orders available.")
else:
    for _, row in orders.iterrows():
        c1, c2, c3, c4, c5 = st.columns([1, 1, 3, 1, 2])

        c1.write(f"**Order ID:** {row['id']}")
        c2.write(f"**Room:** {row['room_number']}")
        c3.write(f"**Items:** {row['ordered_items']}")
        c4.write(f"₹{row['total_amount']}")

        status = c5.selectbox(
            "Status",
            ["Placed", "Preparing", "Delivered"],
            index=["Placed", "Preparing", "Delivered"].index(row["status"]),
            key=f"order_status_{row['id']}"
        )

        if c5.button("Update", key=f"update_order_{row['id']}"):
            requests.post(
                f"{BACKEND_URL}/dashboard/update-order-status",
                params={"order_id": row["id"], "status": status}
            )
            st.success(f"Order {row['id']} updated")
            st.rerun()

st.divider()

# ============================================================
# 🧹 ROOM SERVICE REQUESTS
# ============================================================
st.header("🧹 Room Service Requests")

services = pd.read_sql("SELECT * FROM room_service_requests", engine)

if services.empty:
    st.info("No room service requests available.")
else:
    for _, row in services.iterrows():
        c1, c2, c3, c4 = st.columns([1, 1, 3, 2])

        c1.write(f"**Request ID:** {row['id']}")
        c2.write(f"**Room:** {row['room_number']}")
        c3.write(f"**Type:** {row['request_type']}")

        status = c4.selectbox(
            "Status",
            ["Pending", "In Progress", "Completed"],
            index=["Pending", "In Progress", "Completed"].index(row["status"]),
            key=f"service_status_{row['id']}"
        )

        if c4.button("Update", key=f"update_service_{row['id']}"):
            requests.post(
                f"{BACKEND_URL}/dashboard/update-service-status",
                params={"request_id": row["id"], "status": status}
            )
            st.success(f"Request {row['id']} updated")
            st.rerun()
