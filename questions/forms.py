from django import forms
from .models import Subject, Chapter

class QuestionPaperForm(forms.Form):
    class_level = forms.IntegerField(label="Class Level", min_value=3, max_value=12)
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    chapters = forms.ModelMultipleChoiceField(queryset=Chapter.objects.none())
    total_mcq_marks = forms.IntegerField(label="Total MCQ Marks", required=False)
    total_written_marks = forms.IntegerField(label="Total Written Marks", required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['chapters'].queryset = Chapter.objects.filter(subject_id=subject_id)
            except (ValueError, TypeError):
                pass
