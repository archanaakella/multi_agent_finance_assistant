#!/bin/bash

# Run retriever agent on port 8000
uvicorn agents.retriever_agent:app --host 0.0.0.0 --port 8000 &

# Run orchestration agent on port 8001
uvicorn orchestration_app:app --host 0.0.0.0 --port 8001 &

# Run Streamlit app on port 8501
streamlit run streamlit_app/main.py --server.port=8501 --server.address=0.0.0.0