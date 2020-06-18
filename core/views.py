from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from users.models import User
from .forms import QuestionForm, AnswerForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'core/index.html', {'questions': questions})

def profile_page(request):
    questions = request.user.questions.all()
    answers = Answer.objects.all()
    return render(request, 'core/profile_page.html', {'questions': questions, 'answers': answers})

def question_detail(request, question_pk):
    question = get_object_or_404(Question.objects.all(), pk=question_pk)
    answers = Answer.objects.all()
    return render(request, 'core/question_detail.html', {'question': question, 'answers':answers})

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

def delete_question(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        question.delete()
        return redirect(to='index')

    return render(request, 'core/delete_question.html', {'question': question})