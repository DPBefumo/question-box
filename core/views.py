from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from users.models import User
from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def profile_page(request):
    return render(request, 'core/profile_page.html')

def question_detail(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)
    return render(request, 'core/question_detail.html', {'question': question})

def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to='question_detail', question_pk=question.pk)
    else:
        form = QuestionForm()
    
    return render(request, 'core/new_question.html', {'form': form})

def new_answer(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect(to='question_detail', question_pk=question.pk)
    else:
        form = AnswerForm()

    return render(request, 'core/new_answer.html', {'form': form, 'question': question})