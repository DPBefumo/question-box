from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, search_questions_for_user
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
    answers = question.answers.all()
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
            answer.author = request.user
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

def search_questions(request):
    query = request.GET.get('q')
    
    if query is not None:
        questions = search_questions_for_user(request.user, query)
    else:
        questions = None

    return render(request, "core/search.html", {"questions": questions, "query": query})

# def search_answers(request):
#     query = request.GET.get('q')

#     if query is not None:
#         answers = search_answers_for_user(request.user, query)
#     else:
#         answers = None
    
#     return render(request, "core/search.html", {"answers": answers, "query": query})

# def search_questions_and_answers(request, **kwargs):
#     query = request.GET.get('q')
    
#     if query is not None:
#         questions = search_questions_for_user(request.user, query)
#         answers = search_answers_for_user(request.user, query)
#     else:
#         questions = None
#         answers = None

#     return render(request, "core/search.html", {"questions": questions, "answers": answers, "query": query})