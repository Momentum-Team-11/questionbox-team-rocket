from .models import Question, Answer, User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )

class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "question",
            "created",
            "user",
            "favorited",
        )

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Answer
        fields = (
            "pk",
            "answer",
            "created",
            "question",
            "user",
            "favorited",
            "accepted",
        )

class QuestionAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False)
    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "answers",
        )