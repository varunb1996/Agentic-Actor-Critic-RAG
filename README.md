# Advanced Agentic Actor-Critic GraphRAG System

An advanced end-to-end Agentic RAG system built using FastAPI, Streamlit, ChromaDB, Hybrid Search, GraphRAG, Actor-Critic Agents, Tool Calling, and Autonomous Planning.

This project demonstrates how modern GenAI systems can combine retrieval, reasoning, planning, memory, and multi-agent workflows into a production-style architecture.

---

# Features

## Agentic AI Workflow
- Autonomous planner agent
- Actor agent for response generation
- Critic agent for answer validation and refinement
- Multi-agent orchestration

## Advanced Retrieval
- Vector search using ChromaDB
- BM25 keyword retrieval
- Hybrid retrieval (BM25 + semantic vectors)
- Multi-hop retrieval pipeline
- GraphRAG context expansion

## Knowledge Processing
- PDF ingestion pipeline
- Recursive chunking
- Sentence-transformer embeddings
- Dynamic graph construction using NetworkX

## Tool Calling
- Web search tool
- Calculator tool
- File handling tools

## Memory System
- Conversational memory
- Persistent memory-ready architecture
- Redis-compatible design

## Observability
- LangSmith-ready architecture
- Structured logging support

## MCP Integration
- MCP-ready modular architecture for external tool integration

## Frontend + Backend
- FastAPI backend
- Streamlit frontend UI
- Modular API structure

---

# Tech Stack

| Layer | Technologies |
|---|---|
| Backend | FastAPI, Python |
| Frontend | Streamlit |
| Vector DB | ChromaDB |
| Embeddings | SentenceTransformers |
| Retrieval | BM25, Hybrid Search |
| GraphRAG | NetworkX |
| LLM APIs | OpenRouter |
| Tool Calling | Tavily Search |
| PDF Processing | PyPDF |
| Environment | dotenv |
| Deployment Ready | Docker / Kubernetes compatible |

---

# Project Structure

```bash
agentic-actor-critic-rag/
│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── cache/
│   ├── data/
│   ├── rag/
│   ├── tools/
│   ├── utils/
│   ├── chroma_db/
│   ├── requirements.txt
│   └── test_ingest.py
│
├── frontend/
│   └── app.py
│
└── README.md
```

---

# System Workflow

1. User enters query in Streamlit UI
2. FastAPI backend receives request
3. Planner Agent creates execution plan
4. Hybrid Retriever fetches:
   - Vector results
   - BM25 results
   - Graph-expanded context
5. Web search agent gathers external information
6. Actor Agent generates answer
7. Critic Agent validates response quality
8. Final response returned to frontend
9. Memory module stores conversation context

---

# Installation

## Clone Repository

```bash
git clone <your_repo_url>
cd agentic-actor-critic-rag
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside `backend/`

```env
OPENROUTER_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

---

# Add PDFs

Place all PDFs inside:

```bash
backend/data/
```

---

# Run Ingestion Pipeline

```bash
python test_ingest.py
```

This will:
- Read PDFs
- Chunk documents
- Generate embeddings
- Store vectors in ChromaDB
- Build BM25 index
- Construct GraphRAG graph

---

# Run Backend

```bash
uvicorn api.main:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

---

# Run Frontend

Open a new terminal:

```bash
cd frontend
streamlit run app.py
```

Frontend runs at:

```bash
http://localhost:8501
```

---

# Example Queries

- What is an API?
- Summarize the uploaded research papers
- Explain GraphRAG architecture
- Compare REST APIs and GraphQL
- What are the key findings from the uploaded PDFs?

---

# Future Improvements

- Redis cloud integration
- LangSmith observability dashboards
- Docker deployment
- Kubernetes orchestration
- Multi-modal RAG
- Agent memory persistence
- MCP server integration
- Neo4j-based GraphRAG
- Autonomous tool planning

---

# Why This Project Matters

This project demonstrates:
- Production-style GenAI engineering
- Multi-agent orchestration
- Advanced RAG pipelines
- Graph-based reasoning
- Hybrid retrieval systems
- Tool-augmented LLM workflows
- Scalable AI architecture design

It is designed as a portfolio-grade project for:
- GenAI Engineer roles
- AI Platform Engineer roles
- Applied AI positions
- RAG/LLM Engineer roles
- AI Research Engineering roles

---

# Author

Varun Bukka  
AI / ML / GenAI Engineer
