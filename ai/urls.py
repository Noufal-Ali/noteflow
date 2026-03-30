from django.urls import path
from .views import SummarizeNoteView, ChatWithNotesView

urlpatterns = [
    path('summarize/', SummarizeNoteView.as_view()),
    path('chat/', ChatWithNotesView.as_view()),

]