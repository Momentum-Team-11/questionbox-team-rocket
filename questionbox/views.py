from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import User, Question, Answer
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, QuestionAnswerSerializer
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet 


# =================================================================================
# VIEWSETS
# =================================================================================


class QuestionViewSet(ModelViewSet):
    '''
    List all questions:                   GET / questions /
    Retrieve a specific question:         GET / questions / {id}
    Add a new question:                   POST / questions /
    Update an existing question:          PUT / questions / {id}
    Update part of an existing question:  PATCH / questions / {id}
    Remove a question:                    DELETE / questions / {id} /
    '''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     return Question.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnswerViewSet(ModelViewSet):
    '''
    List all answers:                   GET / answers /
    Retrieve a specific answer:         GET / answers / {id}
    Add a new answer:                   POST / answers /
    Update an existing answer:          PUT / answers / {id}
    Update part of an existing answer:  PATCH / answers / {id}
    Remove a answer:                    DELETE / answers / {id} /
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     return Answer.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# =================================================================================
# CONCRETE VIEWES
# =================================================================================


class UserList(generics.ListCreateAPIView):
    '''
    Return list of all users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    
    
    
    
    
# class QuestionView(generics.CreateAPIView):
#     '''
#     post or get an individual question
#     '''
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [AllowAny]

#     def get_queryset(self):
#         filters = Q(user_id=self.request.user)
#         return Question.objects.filter(filters)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class ModifyQuestionView(generics.RetrieveUpdateDestroyAPIView):
#     '''
#     retrieve, update or delete a single question
#     '''
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [AllowAny]


# class ListAllQuestionsView(generics.ListAPIView):
#     '''
#     List all questions accross application
#     '''
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [AllowAny]


# class UserQuestionsView(generics.ListAPIView):
#     '''
#     List all questions accross application
#     '''
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [AllowAny]


# # =================================================================================
# # Old Views
# # =================================================================================
# class QuestionList(generics.ListCreateAPIView):
#     '''
#     Return list of all questions accross all users
#     '''
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer
#     permission_classes = [AllowAny]


# class UserQuestionView(generics.ListCreateAPIView): 
#     ''''
#     Create a new Question
#     Return a list of all a Users Questions
#     '''
#     serializer_class = QuestionSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['question']
    
#     def get_queryset(self):
#         filters = Q(user_id=self.request.user)
#         return Question.objects.filter(filters)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class UserAnswerView(generics.ListCreateAPIView): 
#     ''''
#     Create a new Answer
#     Return a list of all a Users Answers
#     '''
#     serializer_class = AnswerSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['answer']
    
#     def get_queryset(self):
#         filters = Q(user_id=self.request.user)
#         return Answer.objects.filter(filters)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)




# class AllAnswerList(generics.ListCreateAPIView):
#     '''
#     Return list of all Answers accross all users
#     NOTE: Delete this after we start to refine views
#     '''
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     permission_classes = [AllowAny]


# class AnswerList(generics.ListCreateAPIView):
#     '''
#     Return a list of all the answers a user has
#     given as well as the questions they were to
#     '''
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     permission_classes = [AllowAny]


# class ChangeAnswer(generics.RetrieveUpdateDestroyAPIView):
    # '''
    # Change details of an answer
    # '''
    # queryset = Answer.objects.all()
    # serializer_class = AnswerSerializer
    # permission_classes = [AllowAny]