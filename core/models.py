from django.db import models
from users.models import User
from django.db.models import Q

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answers', null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers', null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    correct_marker = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.body}"

def search_questions_for_user(user, query):
    return user.questions.filter(Q(title__icontains=query) | Q(body__icontains=query))