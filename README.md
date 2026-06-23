# AI Book Companion

An AI-powered reading assistant that helps readers understand and discuss books without revealing spoilers beyond their current progress.

## Overview

AI Book Companion is designed to provide readers with personalised AI assistance while preserving the experience of discovering a story.

The system tracks the reader's progress and aims to generate helpful explanations, discussions, and insights while preventing unwanted spoilers.

## Problem

Traditional AI assistants can accidentally reveal future events when discussing books.

This project explores how AI can provide useful reading support while respecting the reader's current position in a story.

## Features

### Current
- Ask questions about a book
- Track reading progress
- Spoiler-aware responses
- AI-powered discussion

### Planned
- PDF and EPUB book uploads
- Retrieval-Augmented Generation (RAG)
- Multiple book support
- User profiles
- Reading analytics
- Project Architecture

## Current MVP:

User → Streamlit Interface → AI Processing Layer → Prompt Logic → AI Model → Spoiler-Aware Response

## Future:

Book Upload → Text Extraction → Chapter Processing → Embeddings → Vector Database → Retrieval-Augmented Generation → AI Response

## Tech Stack

Programming
Python
Frontend
Streamlit
AI
OpenAI / Gemini API
Prompt Engineering
Retrieval-Augmented Generation (RAG)
Data Processing
LangChain
ChromaDB
Development
GitHub
Git
Virtual Environments

## Project Structure

ai-book-companion/

│
├── frontend/
│   └── app.py
│
├── backend/
│   ├── main.py
│   ├── routes.py
│   └── api.py
│
├── ai/
│   ├── prompts.py
│   ├── chatbot.py
│   ├── spoiler_detector.py
│   └── rag.py
│
├── database/
│   ├── models.py
│   └── storage.py
│
├── books/
│   └── processor.py
│
├── tests/
│
├── docs/
│   ├── architecture.md
│   └── project-plan.md
│
├── requirements.txt
├── .env.example
└── README.md

## Roadmap

### Phase 1 — MVP Prototype
 Create GitHub repository
 Create project structure
 Build basic interface
 Connect AI model
 Generate AI responses

### Phase 2 — Spoiler Prevention
 Track reader progress
 Create spoiler detection logic
 Improve AI prompting
 Test spoiler handling

### Phase 3 — Advanced AI Features
 Add PDF/EPUB uploads
 Extract book content
 Implement RAG pipeline
 Add vector database

### Phase 4 — Deployment
 Deploy application
 Improve UI/UX
 Add user accounts
 Add reading analytics

## Future Vision

The long-term goal is to create an intelligent reading companion that understands a reader's journey through a book and provides personalised assistance without ruining the experience.

## License

This project is licensed under the MIT License.