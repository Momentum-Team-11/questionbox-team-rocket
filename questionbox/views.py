from rest_framework import generics
from .models import User, Question, Answer
from .serializers import UserSerializer, QuestionSerializer, AnswerSerializer, QuestionAnswerSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


# =================================================================================
# VIEWSETS
# =================================================================================


class QuestionViewSet(ModelViewSet):
    '''
    List all questions with answers:      GET / questions /
    Retrieve a specific question:         GET / questions / {id}
    Add a new question:                   POST / questions /
    Update an existing question:          PUT / questions / {id}
    Update part of an existing question:  PATCH / questions / {id}
    Remove a question:                    DELETE / questions / {id} /
    Get list of favorited questions:      GET / questions / favorited /
    Get list of a Users Questions:        GET / questions / user /
    '''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        '''
        specify query set
        '''
        return Question.objects.all()

    def perform_create(self, serializer):
        '''
        save the user from the request to the question created
        '''
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return QuestionAnswerSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=["get"])
    def favorited(self, request):
        '''
        Using this to create a seperate, custom 
        enpoint for favorited questions accessed at:
        GET  /questions/favorited/
        '''
        questions = self.get_queryset().filter(favorited=True).filter(user_id=self.request.user)
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def user(self, request):
        '''
        Using this to create a seperate, custom 
        enpoint for only a Users questions
        GET  /questions/favorited/
        '''
        questions = self.get_queryset().filter(user_id=self.request.user)
        serializer = self.get_serializer(questions, many=True)
        return Response(serializer.data)


class AnswerViewSet(ModelViewSet):
    '''
    List all answers:                   GET / answers /
    Retrieve a specific answer:         GET / answers / {id}
    Add a new answer:                   POST / answers /
    Update an existing answer:          PUT / answers / {id}
    Update part of an existing answer:  PATCH / answers / {id}
    Remove a answer:                    DELETE / answers / {id} /
    Get list of accepted answers:       GET / answers / accepted /
    Get list of a Users answers:        GET / answers / user /
    '''
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        '''
        specify queryset
        '''
        # return Answer.objects.filter(user_id=self.request.user)
        return Answer.objects.all()

    def perform_create(self, serializer):
        '''
        save the user from the request to the answer created
        '''
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def accepted(self, request):
        '''
        Using this to create a seperate, custom 
        enpoint for accepted answers accessed at:
        GET  /answers/accepted/
        '''
        answers = self.get_queryset().filter(accepted=True)
        serializer = self.get_serializer(answers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def user(self, request):
        '''
        Using this to create a seperate, custom 
        enpoint for only a Users questions
        GET  /answers/user/
        '''
        answers = self.get_queryset().filter(user_id=self.request.user)
        serializer = self.get_serializer(answers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def favorited(self, request):
        '''
        Using this to create a seperate, custom 
        enpoint for accepted answers accessed at:
        GET  /answers/favorited/
        '''
        answers = self.get_queryset().filter(favorited=True).filter(user_id=self.request.user)
        serializer = self.get_serializer(answers, many=True)
        return Response(serializer.data)

        

# =================================================================================
# CONCRETE VIEWS
# =================================================================================


class UserList(generics.ListCreateAPIView):
    '''
    Return list of all users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
