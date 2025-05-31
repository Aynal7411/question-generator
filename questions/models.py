from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    class_level = models.PositiveIntegerField()  # Class 3 to 12

    def __str__(self):
        return f"Class {self.class_level} - {self.name}"

class Question(models.Model):
    QUESTION_TYPES = (
        ('mcq', 'MCQ'),
        ('written', 'Written'),
    )

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    text = models.TextField()
    options = models.JSONField(null=True, blank=True)  # Only for MCQ
    answer = models.TextField()
    marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.question_type.upper()} - {self.text[:50]}"
