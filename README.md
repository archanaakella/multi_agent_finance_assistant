# multi_agent_finance_assistant
A finance assistant using AI agents

https://multiagentfinanceassistant-fmg8xegdl4imypf5ff6sk2.streamlit.app/

Features
- **Market Data Retrieval:** Uses **APIs, web scraping, document loaders** to ingest financial insights.
- **Retrieval-Augmented Generation (RAG):** Indexes embeddings in **FAISS** for precise retrieval.
- **Multi-Agent Architecture:** Specialized agents for **API calls, scraping, analytics, LLM-based generation, voice I/O**.
- **Voice-Based Queries:** Supports **speech-to-text (STT) & text-to-speech (TTS)** for verbal market updates.
- **FastAPI Microservices:** Enables scalable multi-agent coordination.


# Tech Stack
- **AI Agents:** LangGraph
- **Vector Store:** FAISS for real-time financial embeddings
- **LLM Processing:** OpenAI/GPT-based financial summaries
- **Data Sources:** AlphaVantage API
- **Backend:** FastAPI for orchestration
- **Frontend:** Streamlit for user interaction
- **Deployment:** Streamlit Community Cloud
