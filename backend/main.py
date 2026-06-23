from fastapi import FastAPI
from pydantic import BaseModel

from ai.chatbot import answer_question


app = FastAPI(
    title="AI Book Companion API"
)


class Question(BaseModel):
    book: str
    chapter: int
    question: str


@app.get("/")
def home():
    return {
        "message": "Backend running"
    }


@app.post("/ask")
def ask_ai(data: Question):

    answer = answer_question(
        data.question,
        data.book,
        data.chapter
    )

    return {
        "answer": answer
    }