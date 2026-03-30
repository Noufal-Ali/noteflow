import logging
from venv import logger
import google.generativeai as genai
from django.conf import settings

logger = logging.getLogger(__name__)
genai.configure(api_key=settings.GEMINI_API_KEY)
models = genai.list_models()
    
model =genai.GenerativeModel('gemini-2.5-flash')

def summarize_text(text):
    logger.info("Initiating summarization for text: %s", text)
    response = model.generate_content(f"Summarize this:\n{text}")
    logger.info("Summarization completed successfully")
    return response.text

def chat_with_notes(query, notes_text):
    logger.info("Initiating chat with query: %s and notes length: %d", query, len(notes_text))
    prompt = f"""
    You are a chat assistant.
    Answer the question based on the notes below.

    Notes:
    {notes_text}

    Question:
    {query}
    """

    response = model.generate_content(prompt)
    logger.info("Chat response generated successfully")
    return response.text

