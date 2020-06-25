from rest_framework import serializers
from users.models import User
from core.models import Question, Answer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'image',
            'username',
            'email',
            'is_staff',
            'location',
            'bio',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'author',
            'question',
            'title',
            'body',
            'marked_correct',
        ]

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'url',
            'user',
            'title',
            'body',
            'favorited_by',
            'answers',
        ]

    # def create(self, validated_data):
    #     """
    #     Create and return a new 'Question' instance, given the validated data
    #     """
    #     answers = validated_data.pop('answers', [])
    #     question = Question.objects.create(**validated_data)
    #     for answer in answers:
    #         question.answers.create(**answer)
    #     return question

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing 'Question' instance, given the validated data
    #     """
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.body = validated_data.get('body', instance.body)
    #     instance.save()
    #     return instance