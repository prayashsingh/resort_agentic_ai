import os
from openai import OpenAI
from dotenv import load_dotenv

# -------------------------------------------------
# Load environment variables from .env file
# -------------------------------------------------
load_dotenv()

# -------------------------------------------------
# Read API key
# -------------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. "
        "Please add it to your .env file or environment variables."
    )

# -------------------------------------------------
# Initialize OpenAI client
# -------------------------------------------------
client = OpenAI(api_key=OPENAI_API_KEY)

# -------------------------------------------------
# Unified LLM call function
# -------------------------------------------------
def call_llm(messages, tools=None):
    """
    messages: List of dicts [{"role": "user"/"assistant"/"system", "content": "..."}]
    tools: Optional OpenAI function-calling schema
    """
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )
