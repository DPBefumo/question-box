from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    # profile = models.URLField
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    
    def is_favorite_answer(self, answer):
        return self.favorite_answer.filter(pk=answer.pk).count() == 1
