from django.shortcuts import render
from rest_framework import generics
from .models import User, Question, Answer
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, QuestionAnswerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    '''
    Set the root API endpoint
    Modeled after: https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners
    '''
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
        'answers': reverse('answer-list', request=request, format=format)
    })


class UserList(generics.ListCreateAPIView):
    '''
    Return list of all users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionList(generics.ListCreateAPIView):
    '''
    Return list of all questions accross all users
    '''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AllAnswerList(generics.ListCreateAPIView):
    '''
    Return list of all Answers accross all users
    NOTE: Delete this after we start to refine views
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerList(generics.ListCreateAPIView):
    '''
    Return a list of all the answers a user has
    given as well as the questions they were to
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ChangeAnswer(generics.RetrieveUpdateDestroyAPIView):
    '''
    Change details of an answer
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer