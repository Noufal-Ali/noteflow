import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
models = genai.list_models()
    
model =genai.GenerativeModel('gemini-2.5-flash')

def summarize_text(text):

    response = model.generate_content(f"Summarize this:\n{text}")
    return response.text

def chat_with_notes(query, notes_text):
    prompt = f"""
    You are a chat assistant.
    Answer the question based on the notes below.

    Notes:
    {notes_text}

    Question:
    {query}
    """

    response = model.generate_content(prompt)
    return response.text

