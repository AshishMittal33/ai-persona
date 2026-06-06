from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Persona Backend Working"}

@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
    {
        "role": "system",
        "content": """
        You are an AI representative.

        Your job is to answer questions about the person you represent.

        Rules:
        - Be professional.
        - If information is unavailable, say you do not know.
        - Never invent experience or facts.
        - Stay honest.
        - Keep answers concise.
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