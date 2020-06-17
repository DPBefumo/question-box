from django import forms
from models import Question, Answer

class QuestionForm(form.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'body',
            'time_stamp'
        ]

class AnswerForm(form.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'question',
            'body',
            'time_stamp',
            'correct_marker',
        ]