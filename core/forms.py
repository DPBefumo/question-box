from django import forms
from .models import Question, Answer, User

class QuestionForm(forms.ModelForm):
    tag_names = forms.CharField(label='Tags', help_text='Separate tags with a space', widget=forms.TextInput(attrs={'class': ''}))
    
    class Meta:
        model = Question
        fields = [
            'title',
            'body',
        ]

class AnswerForm(forms.ModelForm):

    
    class Meta:
        model = Answer
        fields = [
            'title',
            'body',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'image',
        ]