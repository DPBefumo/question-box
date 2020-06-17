from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def profile_page(request):
    return render(request, 'core/profile_page.html')