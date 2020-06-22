from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, search_questions_for_user, Tag
from django.contrib.auth.decorators import login_required
from users.models import User
from .forms import QuestionForm, AnswerForm, UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'core/index.html', {'questions': questions,})

@login_required
def profile_detail(request, user_pk):
    profile = get_object_or_404(User.objects.all(), pk=user_pk)
    questions = request.user.questions.all()
    answers = Answer.objects.all()
    return render(request, 'core/profile_detail.html', {'profile': profile, 'questions': questions, 'answers': answers})

@login_required
def edit_profile(request, user_pk):
    profile = get_object_or_404(User.objects.all(), pk=user_pk)

    if request.method == 'POST':
        form = UserForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            user = form.save()
            return redirect(to='profile_detail', user_pk=user.pk)
    
    else:
        form = UserForm(instance=profile)
    
    return render(request, 'core/edit_profile.html', {'form': form, 'profile': profile})



def question_detail(request, question_pk):
    question = get_object_or_404(Question.objects.all(), pk=question_pk)
    answers = question.answers.all()
    user_favorite_question = False
    if request.user.is_authenticated:
        user_favorite_question = request.user.is_favorite_question(question)
    
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

    return render(request, 'core/question_detail.html', {'question': question, 'answers':answers, 'user_favorite_question': user_favorite_question, 'form': form})

@login_required
def new_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            question.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to='question_detail', question_pk=question.pk)
    else:
        form = QuestionForm()
    
    return render(request, 'core/new_question.html', {'form': form})

@login_required
def add_answer(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

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

    return render(request, 'core/add_answer.html', {'form': form, 'question': question})

@login_required
def delete_question(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == 'POST':
        question.delete()
        return redirect(to='index')

    return render(request, 'core/delete_question.html', {'question': question})


def show_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    questions = tag.questions.filter(user=request.user)
    return render(request, 'core/tag_detail.html', {'tag': tag, 'questions': questions})


def search_questions(request):
    query = request.GET.get('q')
    
    if query is not None:
        questions = search_questions_for_user(request.user, query)
    else:
        questions = None

    return render(request, "core/search.html", {"questions": questions, "query": query})

@csrf_exempt
def toggle_favorite_question(request, question_pk):
    question = get_object_or_404(Question.objects.all(), pk=question_pk)

    if request.user.is_favorite_question(question):
        request.user.favorite_questions.remove(question)
        return JsonResponse({"isFavorite": False})
    else:
        request.user.favorite_questions.add(question)
        return JsonResponse({"isFavorite": True})

@csrf_exempt
def mark_answer_correct(request, question_pk, answer_pk):
    questions = Questions.objects.all()
    question = get_object_or_404(questions, pk=question_pk)
    answers = question.answers.all()
    answer = get_object_or_404(answers, pk=answer_pk)

    if answer.marked_correct == True:
        answer.marked_correct=False
        answer.save()
        return JsonResponse({"markedCorrect": False})
    else:
        answer.marked_correct=True
        answer.save()
        return JsonResponse({"markedCorrect": True})
