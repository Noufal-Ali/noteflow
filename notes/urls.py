from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns =router.urls
