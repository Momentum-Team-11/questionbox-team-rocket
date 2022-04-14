from .models import Question, Answer, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    '''
    Serialize Data for the User model
    '''
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class QuestionSerializer(serializers.ModelSerializer):
    '''
    Serialize Data for the Question model
    '''
    # user_created = serializers.SlugRelatedField(slug_field='username', read_only=True, source='user')
    favorited = serializers.SlugRelatedField(slug_field="username", read_only=True, many=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "question",
            "user",
            "favorited",
        )


class AnswerSerializer(serializers.ModelSerializer):
    '''
    Serialize Data for the Answer model
    # user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    '''
    user = serializers.SerializerMethodField()
    favorited = serializers.SlugRelatedField(slug_field="username", read_only=True, many=True)

    def get_user(self, obj):
        return obj.user.username
# favorited = serializers.SlugRelatedField(slug_field='favorited')
    # favorited = serializers.SlugRelatedField(slug_field='username', read_only='True', source='user', many=True)
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Answer
        fields = (
            "pk",
            "question",
            "answer",
            "created",
            "user",
            "favorited",
            "accepted",
        )


class FavoriteAnswerSerializer(serializers.ModelSerializer):
    '''
    Serialize Data for the Answer model
    '''
    question = QuestionSerializer(many=False, required=True)
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Answer
        fields = (
            "pk",
            "question",
            "answer",
            "created",
            "user",
            "favorited",
            "accepted",
        )
        


class QuestionAnswerSerializer(serializers.ModelSerializer):
    '''
    Serialize Data for a Question and all of its Answers
    '''
    answers = AnswerSerializer(many=True, required=False, source='questions')
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    favorited = serializers.SlugRelatedField(slug_field="username", read_only=True, many=True)

    class Meta:
        model = Question
        fields = (
            "pk",
            "title",
            "question",
            "created",
            "user",
            "favorited",
            "answers",
        )
