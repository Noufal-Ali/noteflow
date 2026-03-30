def summarize_text(text):
    word = text.split()
    return "(Mock)" + "".join(word[:20]) + "..."

def chat_with_notes(query, notes_text):
    return f"(Mock AI) You asked: '{query}', Based on the notes: {notes_text[:100]}..."
