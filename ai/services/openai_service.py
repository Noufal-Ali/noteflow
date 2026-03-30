import logging
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)
logger = logging.getLogger(__name__)

def summarize_text(text):
    logger.info("Initiating summarization for text: %s", text)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize briefly"},
            {"role": "user", "content": text}
        
        ],
    )
    logger.info("Summarization completed successfully")
    return response.choice[0].message.content

def chat_with_notes(query, notes_text):
    logger.info("Initiating chat with query: %s and notes length: %d", query, len(notes_text))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer the question based on the notes."},
            {"role": "user", "content": f"Notes:\n{notes_text}\n\nQuestion:\n{query}"}
        
        ],
    )
    logger.info("Chat response generated successfully")
    return response.choice[0].message.content