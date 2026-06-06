from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
from rag import search
import os

# Load environment variables
load_dotenv()

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# FastAPI App
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple Conversation Memory
conversation_history = []


# Request Model
class ChatRequest(BaseModel):
    message: str


# Home Route
@app.get("/")
def home():
    return {
        "message": "AI Persona Backend Working"
    }


# Chat Route
@app.post("/chat")
def chat(request: ChatRequest):

    # Retrieve relevant knowledge
    result = search(request.message)

    knowledge = "\n\n".join(
        result["documents"]
    )

    # Build messages
    messages = [
        {
            "role": "system",
            "content": f"""
You are an AI representative.

Knowledge:
{knowledge}

Rules:
- Only answer from the provided knowledge.
- If the answer is not present in the knowledge, say:
  "I do not have enough information."
- Never invent facts.
- Be concise and professional.
"""
        }
    ]

    # Add conversation history
    messages.extend(conversation_history)

    # Current user message
    messages.append(
        {
            "role": "user",
            "content": request.message
        }
    )

    # Call Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content

    # Save conversation
    conversation_history.append(
        {
            "role": "user",
            "content": request.message
        }
    )

    conversation_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # Keep only recent messages
    if len(conversation_history) > 10:
        conversation_history.pop(0)

    return {
        "reply": answer,
        "sources": result["ids"]
    }