from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, ChapterViewSet, QuestionViewSet, question_list, generate_question_paper

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet)
router.register(r'chapters', ChapterViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', question_list, name='question_list'),
     path('generate-paper/', generate_question_paper, name='generate_paper'),
]
