import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notes.models import Note
from ai.services.provider import summarize_text, chat_with_notes

logger = logging.getLogger(__name__)

class SummarizeNoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        note_id = request.data.get("note_id")
        logger.info("Summarization request for note_id: %s by user: %s", note_id, request.user)

        if not note_id:
            logger.error("note_id is required for summarization")
            return Response({"error":{
                                    "error_code": 2010,
                                    "message":"note_id is required"
                                    }}, status=400)
        
        try:
            note = Note.objects.get(id=note_id, user=request.user)
        except Note.DoesNotExist:
            logger.error("Note with id %s not found for user %s", note_id, request.user)
            return Response({"error":{
                                    "error_code": 2011,
                                    "message":"Note not found"
                                    }}, status=404)
        
        summary = summarize_text(note.content)
        logger.info("Summarization successful")
        return Response({
            "summary": summary
            })
    

class ChatWithNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        query = request.data.get("query")
        logger.info("Chat request received with query: %s by user: %s", query, request.user)

        if not query:
            logger.error("Query is required for chat")
            return Response({"error":{
                                    "error_code": 2022,
                                    "message": "Query is required"
                                    }}, status=400)
        
        notes = Note.objects.filter(user=request.user)
        notes_text = "\n".join([note.content for note in notes])

        response = chat_with_notes(query, notes_text)
        logger.info("Chat response generated for user: %s", request.user)

        return Response({
            "response": response
            })