from langchain_community.llms import OpenAI
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-4-turbo", openai_api_key="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")

def generate_market_brief(context):
    """Synthesize financial insights into narrative form."""
    prompt = f"Summarize today's key financial events based on: {context}"
    return llm.predict(prompt)