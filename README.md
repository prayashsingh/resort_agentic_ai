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


🤖 2. Agent Flow (How the System Works)
Step-by-Step Flow

Guest sends a message via chat UI

Message reaches FastAPI /chat endpoint

Session memory is loaded using session_id

LangGraph starts orchestration

Intent Router analyzes the message

Correct agent is selected:

Receptionist Agent

Restaurant Agent

Room Service Agent

Agent may:

Ask follow-up questions

Call tools (DB, calculators)

Store/update data

Final response is returned to user

Data is reflected in the dashboard


🤖3. Agents (Very Short)

Receptionist Agent → Handles check-in/check-out, facilities info, and room availability

Restaurant Agent → Shows menu, takes food orders, calculates bill, stores orders

Room Service Agent → Handles cleaning, laundry, and extra amenities requests

Each agent is auto-selected by the intent router and supports multi-turn chat using session memory.



🛠 4. Tech Stack Used

<img width="699" height="520" alt="Screenshot 2025-12-28 031057" src="https://github.com/user-attachments/assets/e153b729-4e7c-4438-9015-d46da76acbda" />



🚀 5. How to Run the Project Locally
🔹 Step 1: Clone Repository
          git clone https://github.com/your-username/resort-agentic-ai.git
          cd resort-agentic-ai

🔹 Step 2: Create Virtual Environment
          python -m venv venv
          venv\Scripts\activate   # Windows

🔹 Step 3: Install Dependencies
          pip install -r requirements.txt

🔹 Step 4: Run Backend Server
          uvicorn app.main:app


Backend runs at:

         http://127.0.0.1:8000

🔹 Step 5: Run Frontend Chat UI (New Terminal)
         streamlit run frontend/chat_ui.py

🔹 Step 6: Run Operations Dashboard (Optional)
         streamlit run dashboard/dashboard.py

