import logging

logger = logging.getLogger(__name__)

def summarize_text(text):
    logger.info("Initiating mock summarization for text: %s", text)
    word = text.split()
    return "(Mock)" + "".join(word[:20]) + "..."

def chat_with_notes(query, notes_text):
    logger.info("Initiating mock chat with query: %s and notes length: %d", query, len(notes_text))
    return f"(Mock AI) You asked: '{query}', Based on the notes: {notes_text[:100]}..."
