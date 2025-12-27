🏨 Resort Agentic AI System
A chat-based agentic AI system designed for a resort to autonomously handle guest requests across Reception, Restaurant, and Room Service using a single unified chat interface.
The system intelligently understands user intent, routes requests to the correct agent, maintains conversational context, performs actions via tools/APIs, persists data, and updates a live operations dashboard.

📌 1. System Architecture

The system follows a modular, layered agentic architecture with clear separation of concerns.

🔹 High-Level Architecture

<img width="710" height="475" alt="Screenshot 2025-12-28 025538" src="https://github.com/user-attachments/assets/4f81c003-5aec-40ef-880d-8b2da204fef8" />


🔹 Key Architectural Principles

Single chat interface for all guest interactions

Agent-based design (each department is a specialized agent)

Context-aware routing using LangGraph

Multi-turn conversations using session memory

Persistent storage using SQLite

Real-time operational visibility via dashboard


