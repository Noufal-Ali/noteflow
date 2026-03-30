from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notes.models import Note
from ai.services.provider import summarize_text, chat_with_notes

class SummarizeNoteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        note_id = request.data.get("note_id")

        if not note_id:
            return Response({"error":{
                                    "error_code": 2010,
                                    "message":"note_id is required"
                                    }}, status=400)
        
        try:
            note = Note.objects.get(id=note_id, user=request.user)
        except Note.DoesNotExist:
            return Response({"error":{
                                    "error_code": 2011,
                                    "message":"Note not found"
                                    }}, status=404)
        
        summary = summarize_text(note.content)
        
        return Response({
            "summary": summary
            })
    

class ChatWithNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        query = request.data.get("query")
        
        if not query:
            return Response({"error":{
                                    "error_code": 2022,
                                    "message": "Query is required"
                                    }}, status=400)
        
        notes = Note.objects.filter(user=request.user)
        notes_text = "\n".join([note.content for note in notes])

        response = chat_with_notes(query, notes_text)

        return Response({
            "response": response
            })