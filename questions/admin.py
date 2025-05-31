from django.contrib import admin
from .models import Subject, Chapter, Question

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'class_level')
    list_filter = ('subject', 'class_level')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'chapter', 'question_type', 'marks')
    list_filter = ('question_type', 'chapter__subject', 'chapter__class_level')
    search_fields = ('text', 'answer')
