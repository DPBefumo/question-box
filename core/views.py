from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from users.models import User
# from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def profile_page(request):
    return render(request, 'core/profile_page.html')

def question_detail(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)
    return render(request, 'core/question.html', {'question': question})