# =========================================================
# app/main.py
# MASTER ENTRY POINT FOR THE ENTIRE PROJECT
# =========================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -----------------------------
# Database
# -----------------------------
from app.database.db import Base, engine

# -----------------------------
# API Routers
# -----------------------------
from app.api.chat import router as chat_router
from app.api.dashboard_api import router as dashboard_router

# -----------------------------
# Startup Utilities
# -----------------------------
from app.tools.menu_loader import load_menu_from_excel

# =========================================================
# FASTAPI APPLICATION SETUP
# =========================================================

app = FastAPI(
    title="Agentic Resort AI System",
    description="""
    A chat-based agentic AI system for a resort that autonomously
    handles receptionist queries, restaurant orders, and room
    service requests, with a real-time operations dashboard.
    """,
    version="1.0.0"
)

# =========================================================
# MIDDLEWARE (OPTIONAL BUT RECOMMENDED)
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# DATABASE INITIALIZATION
# =========================================================

# Create ALL tables:
# - rooms
# - menu_items
# - orders
# - room_service_requests
Base.metadata.create_all(bind=engine)

# =========================================================
# LOAD RESTAURANT MENU (EXCEL → DATABASE)
# =========================================================

@app.on_event("startup")
def startup_event():
    """
    Runs once when the server starts.
    Loads the restaurant menu from Excel into the database.
    """
    try:
        load_menu_from_excel("data/Restaurant_Menu.xlsx")
        print("✅ Restaurant menu loaded from Excel successfully.")
    except Exception as e:
        print(f"⚠️ Menu loading skipped or failed: {e}")

# =========================================================
# API ROUTERS
# =========================================================

# Single chat interface for guests
app.include_router(chat_router)

# Dashboard APIs (used by Streamlit dashboard)
app.include_router(dashboard_router)

# =========================================================
# HEALTH CHECK ENDPOINT
# =========================================================

@app.get("/")
def health_check():
    """
    Simple health check endpoint.
    """
    return {
        "status": "running",
        "service": "Agentic Resort AI System",
        "version": "1.0.0"
    }
