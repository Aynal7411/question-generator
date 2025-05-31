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

from django.shortcuts import render
from .forms import QuestionPaperForm
from .models import Question
import random

def generate_question_paper(request):
    questions_mcq = []
    questions_written = []
    
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST)
        if form.is_valid():
            class_level = form.cleaned_data['class_level']
            subject = form.cleaned_data['subject']
            chapters = form.cleaned_data['chapters']
            total_mcq = form.cleaned_data['total_mcq_marks'] or 0
            total_written = form.cleaned_data['total_written_marks'] or 0

            chapter_ids = chapters.values_list('id', flat=True)
            
            # MCQ selection
            if total_mcq > 0:
                mcqs = list(
                    Question.objects.filter(
                        chapter_id__in=chapter_ids,
                        question_type='mcq'
                    )
                )
                random.shuffle(mcqs)
                selected_mcqs = []
                marks_accumulated = 0
                for q in mcqs:
                    if marks_accumulated + q.marks <= total_mcq:
                        selected_mcqs.append(q)
                        marks_accumulated += q.marks
                questions_mcq = selected_mcqs

            # Written selection
            if total_written > 0:
                written = list(
                    Question.objects.filter(
                        chapter_id__in=chapter_ids,
                        question_type='written'
                    )
                )
                random.shuffle(written)
                selected_written = []
                marks_accumulated = 0
                for q in written:
                    if marks_accumulated + q.marks <= total_written:
                        selected_written.append(q)
                        marks_accumulated += q.marks
                questions_written = selected_written

    else:
        form = QuestionPaperForm()

    return render(request, 'generate_paper.html', {
        'form': form,
        'questions_mcq': questions_mcq,
        'questions_written': questions_written
    })
