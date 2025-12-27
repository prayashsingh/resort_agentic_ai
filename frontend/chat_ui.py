import streamlit as st
import requests
import uuid

# -----------------------------------
# CONFIG
# -----------------------------------
BACKEND_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="Resort AI Assistant", layout="centered")
st.title("🏨 Resort AI Assistant")

# -----------------------------------
# SESSION MANAGEMENT
# -----------------------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "room_number" not in st.session_state:
    st.session_state.room_number = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------------
# ROOM NUMBER INPUT (ONCE)
# -----------------------------------
if not st.session_state.room_number:
    st.subheader("Enter your room number")
    room = st.text_input("Room Number")

    if st.button("Start Chat"):
        if room.strip():
            st.session_state.room_number = room.strip()
            st.rerun()   # ✅ FIXED HERE
        else:
            st.warning("Please enter a valid room number")

    st.stop()

# -----------------------------------
# CHAT HISTORY DISPLAY
# -----------------------------------
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------------
# USER INPUT
# -----------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # -----------------------------------
    # CALL BACKEND
    # -----------------------------------
    params = {
        "session_id": st.session_state.session_id,
        "room_number": st.session_state.room_number,
        "message": user_input
    }

    try:
        response = requests.post(BACKEND_URL, params=params)
        reply = response.json()["reply"]
    except Exception as e:
        reply = f"⚠️ Error contacting server: {e}"

    # Show assistant message
    st.session_state.chat_history.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
