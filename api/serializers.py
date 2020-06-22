from rest_framework import serializers
from users.models import User
from core.models import Question, Answer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'email',
            'is_staff'
            'location',
            'bio',
        ]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = [
            'url',
            'user',
            'title',
            'body',
            'favorited_by',
        ]
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'url',
            'author',
            'title',
            'body',
            'marked_correct',
        ]