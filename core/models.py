from django.db import models
from users.models import User
from django.contrib.postgres.search import SearchVector
from django.db.models import Q

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.tag

class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    tags = models.ManyToManyField(to=Tag, related_name='questions')
    
    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)

        return " ".join(tag_names)

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)

    def __str__(self):
        return self.title

class Answer(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answers', null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name='answers', null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(max_length=1000)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    correct_marker = models.BooleanField(default=False)
    favorited_by = models.ManyToManyField(to=User, related_name='favorite_answer')
    tags = models.ManyToManyField(to=Tag, related_name='answers')

    def __str__(self):
        return f"{self.body}"


def search_questions_for_user(user, query):
    questions = Question.objects
    return questions.annotate(search=SearchVector('user', 'title', 'body', 'tags')).filter(search=query).distinct('pk')


# def get_tag_names(self):
#     tag_names = []
#     for tag in self.tags.all():
#         tag_names.append(tag.tag)

#     return " ".join(tag_names)

# def set_tag_names(self, tag_names):
#     tag_names = tag_names.split()
#     tags = []
#     for tag_name in tag_names:
#         tag = Tag.objects.filter(tag=tag_name).first()
#         if tag is None:
#             tag = Tag.objects.create(tag=tag_name)
#         tags.append(tag)
#     self.tags.set(tags)

# def search_answers_for_user(user, query, **kwargs):
#     answers = Answer.objects
#     return answers.annotate(search=SearchVector('author', 'title', 'body', 'tags')).filter(search=query).distinct('pk')

# for authorization 
# def get_questions_for_user(queryset, user):
#     if user.is_authenticated:
#         questions = queryset.filter(Q(public=True) | Q(user=user))
#     else:
#         questions = queryset.filter(public=True)
#     return questions