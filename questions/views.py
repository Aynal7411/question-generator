# questions/views.py
from rest_framework import viewsets
from .models import Subject, Chapter, Question
from .serializers import SubjectSerializer, ChapterSerializer, QuestionSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.select_related('chapter').all()
    return render(request, 'question_list.html', {'questions': questions})
