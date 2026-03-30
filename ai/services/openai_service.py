from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize briefly"},
            {"role": "user", "content": text}
        
        ],
    )
    return response.choice[0].message.content

def chat_with_notes(query, notes_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer the question based on the notes."},
            {"role": "user", "content": f"Notes:\n{notes_text}\n\nQuestion:\n{query}"}
        
        ],
    )
    return response.choice[0].message.content