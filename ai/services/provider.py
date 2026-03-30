import os

AI_PROVIDER = os.getenv('AI_PROVIDER', 'mock')

if AI_PROVIDER == 'openai':
    from .openai_service import summarize_text, chat_with_notes
elif AI_PROVIDER == 'gemini':
    from .gemini_service import summarize_text, chat_with_notes
else:
    from .mock_service import summarize_text, chat_with_notes
    