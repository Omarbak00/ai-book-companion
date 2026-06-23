import streamlit as st
import requests

st.title("📚 AI Book Companion")

book = st.text_input("Book")

chapter = st.number_input(
    "Current chapter",
    min_value=1
)

question = st.text_input(
    "Question"
)


if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "book": book,
            "chapter": chapter,
            "question": question
        }
    )

    st.write(response.json()["answer"])