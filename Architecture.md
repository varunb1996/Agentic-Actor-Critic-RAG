# Advanced Agentic Actor-Critic GraphRAG Architecture

---

# High-Level Architecture

```text
                ┌─────────────────────┐
                │     Streamlit UI    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     FastAPI API     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    Planner Agent    │
                └──────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
 ┌──────────────┐ ┌────────────────┐ ┌────────────────┐
 │ Hybrid Search│ │ GraphRAG Agent │ │ Web Search Tool│
 └──────┬───────┘ └────────┬───────┘ └────────────────┘
        │                  │
        ▼                  ▼
 ┌──────────────┐ ┌────────────────┐
 │ Chroma Vector│ │ Knowledge Graph│
 │ Database     │ │ (NetworkX)     │
 └──────────────┘ └────────────────┘
        │
        ▼
 ┌──────────────┐
 │ Actor Agent  │
 └──────┬───────┘
        ▼
 ┌──────────────┐
 │ Critic Agent │
 └──────┬───────┘
        ▼
 ┌──────────────┐
 │ Final Output │
 └──────────────┘
```

---

# Core Components

---

# 1. Frontend Layer

## Technology
- Streamlit

## Responsibilities
- User interaction
- Query submission
- Response visualization
- Planner/Critic output display

---

# 2. API Layer

## Technology
- FastAPI

## Responsibilities
- REST endpoint management
- Request handling
- Agent orchestration
- Communication between frontend and backend

---

# 3. Planner Agent

## Responsibilities
- Understand user intent
- Create execution strategy
- Decide retrieval sequence
- Route tasks to tools and retrievers

## Example Plan

```text
1. Retrieve relevant PDF chunks
2. Expand graph context
3. Search external web sources
4. Generate answer
5. Critique and refine answer
```

---

# 4. Hybrid Retrieval System

## Components
- BM25 retrieval
- Vector similarity retrieval

## Purpose
Combines:
- Keyword precision
- Semantic understanding

## Flow

```text
User Query
    ↓
BM25 Search
    +
Vector Search
    ↓
Merged Ranked Results
```

---

# 5. ChromaDB Vector Store

## Responsibilities
- Store embeddings
- Semantic similarity search
- Persistent vector storage

## Embedding Model

```text
all-MiniLM-L6-v2
```

---

# 6. GraphRAG Layer

## Technology
- NetworkX

## Responsibilities
- Build relationship graph
- Context expansion
- Multi-hop reasoning

## Graph Construction

Nodes:
- Document chunks

Edges:
- Semantic similarity
- Shared entities
- Context relationships

---

# 7. Tool Calling System

## Available Tools

### Web Search Tool
- External knowledge retrieval
- Real-time information

### Calculator Tool
- Mathematical reasoning

### File Tool
- Document operations

---

# 8. Actor Agent

## Responsibilities
- Generate final answer
- Use retrieved context
- Perform reasoning
- Synthesize information

---

# 9. Critic Agent

## Responsibilities
- Validate answer quality
- Detect hallucinations
- Improve response coherence
- Request refinement if needed

## Workflow

```text
Actor Output
      ↓
Critic Evaluation
      ↓
Approved OR Regenerate
```

---

# 10. Memory System

## Responsibilities
- Maintain conversational history
- Support contextual continuity
- Enable long-term interactions

## Current State
- Redis-ready architecture
- Local memory fallback supported

---

# 11. Observability Layer

## LangSmith Integration Ready

Supports:
- Prompt tracing
- Agent debugging
- Execution monitoring
- Chain visualization

---

# 12. MCP Integration Layer

## Purpose
Enable:
- External tool integration
- Agent interoperability
- Standardized AI workflows

---

# Ingestion Pipeline

```text
PDF Files
    ↓
PyPDF Loader
    ↓
Recursive Text Splitter
    ↓
Chunk Creation
    ↓
Sentence Embeddings
    ↓
ChromaDB Storage
    ↓
BM25 Indexing
    ↓
Graph Construction
```

---

# End-to-End Execution Flow

```text
User Query
    ↓
Planner Agent
    ↓
Hybrid Retrieval
    ↓
Graph Expansion
    ↓
Web Search
    ↓
Actor Agent
    ↓
Critic Agent
    ↓
Final Answer
    ↓
Memory Storage
```

---

# Scalability Considerations

## Future Production Upgrades

- Redis Cloud
- Neo4j GraphDB
- PostgreSQL
- Kubernetes
- Docker containers
- Async retrieval pipelines
- Distributed vector search
- Multi-agent scaling

---

# Security Considerations

- Environment variable management
- API key isolation
- Input validation
- Request sanitization
- Rate limiting
- Secure deployment practices

---

# Deployment Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
Agent Layer
        ↓
Retrieval + Tools Layer
        ↓
Vector DB + Knowledge Graph
```

---

# Engineering Highlights

This project demonstrates:

- Agentic AI systems
- Autonomous planning
- Hybrid retrieval
- GraphRAG
- Multi-hop reasoning
- Tool-augmented generation
- Critic-based refinement
- Production-ready architecture patterns

---

# Intended Use Cases

- Enterprise document QA
- Research assistants
- AI copilots
- Knowledge management
- Technical documentation agents
- Multi-document reasoning systems
