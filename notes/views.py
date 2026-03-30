import logging
from venv import logger
from rest_framework import viewsets, filters
from .models import Note, Task
from .serializers import NoteSerializer, TaskSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger(__name__)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    search_fields = ['title', 'content']
    ordering_fields = ['created_at']
    filterset_fields = ['tags']

    def get_queryset(self):
        logger.info("Fetching notes for user: %s", self.request.user)
        return Note.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        logger.info("Creating note for user: %s", self.request.user)
        serializer.save(user=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        logger.info("Fetching tasks for user: %s", self.request.user)
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        logger.info("Creating task for user: %s", self.request.user)
        serializer.save(user=self.request.user)
