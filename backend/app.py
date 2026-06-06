from fastapi import FastAPI
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
    knowledge = search(request.message)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
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
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    answer = response.choices[0].message.content

    return {
        "reply": answer
    }