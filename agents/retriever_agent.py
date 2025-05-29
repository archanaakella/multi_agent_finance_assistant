from fastapi import FastAPI, Query
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

app = FastAPI()

# Load model and FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("finance_vector_store.index")

market_texts = [
    "TSMC beat earnings estimates by 4%",
    "Samsung missed earnings projections by 2%",
    "Asia tech market sentiment is neutral",
    "Rising yields are pressuring valuations"
]

@app.get("/retrieve/")
def retrieve(query: str = Query(...)):
    """Retrieve most relevant financial insight."""
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    
    if I[0][0] < len(market_texts):
        top_result = market_texts[I[0][0]]
    else:
        top_result = "No relevant insights found."

    return {"query": query, "retrieved_insight": top_result}