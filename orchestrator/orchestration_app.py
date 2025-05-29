import logging
import requests
from fastapi import FastAPI
from urllib.parse import unquote
from pydantic import BaseModel

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.get("/retrieve/")
def get_insight(query: str):
    """Fetch financial insight dynamically from the retrieval agent."""
    query = unquote(query)  # Decode query string properly
    logging.info(f"Received retrieval request for: {query}")
    
    # Send request to retrieval service
    response = requests.get(f"http://127.0.0.1:8000/retrieve/?query={query}")
    
    if response.status_code == 200 and "retrieved_insight" in response.json():
        insight = response.json()["retrieved_insight"]
    else:
        insight = "No relevant insights found."

    return {"query": query, "retrieved_insight": insight}

# ----- POST endpoint for voice-based queries -----
class VoiceInput(BaseModel):
    audio_text: str

@app.post("/process_voice/")
async def handle_voice_query(input: VoiceInput):
    """Process voice input, retrieve insights dynamically."""
    text_query = input.audio_text
    logging.info(f"Processing voice query: {text_query}")

    if not text_query:
        return {"error": "Missing voice query!"}

    # Fetch insight dynamically from retrieval service
    response = requests.get(f"http://127.0.0.1:8000/retrieve/?query={text_query}")
    
    if response.status_code == 200 and "retrieved_insight" in response.json():
        insight = response.json()["retrieved_insight"]
    else:
        insight = "No relevant insights found."

    return {"spoken_response": f"Market Update: {insight}"}

# ----- Run the FastAPI server -----
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
