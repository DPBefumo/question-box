from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    web_link = models.URLField(max_length=200, null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)

    
    def is_favorite_question(self, question):
        return self.favorite_questions.filter(pk=question.pk).count() == 1

    def is_favorite_answer(self, answer):
        return self.favorite_answers.filter(pk=answer.pk).count() == 1
