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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answers', null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers', null=True)
    body = models.TextField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    correct_marker = models.BooleanField(default=False)
