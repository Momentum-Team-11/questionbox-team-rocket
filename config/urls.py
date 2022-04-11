from django.contrib import admin
from django.urls import path, include
from questionbox import views
from questionbox.views import AnswerViewSet, QuestionViewSet
from rest_framework import routers


# =================================================================================
# ModelViewSet Routes
# =================================================================================


router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view(), name='user-list'),
    
    # path('answer/', views.UserAnswerView.as_view(), name='answer-create-get'),
    # path('answers/', views.UserAnswerView.as_view(), name='answer-list'),
    # path('answer/<int:answer_pk>', views.ChangeAnswer.as_view(), name='answer-detail'),
]



# ROUTER QUESTION ENDPOINTS
    # List all questions:                  GET / questions /
    # Retrieve a specific question:        GET / questions / {id}
    # Add a new question:                  POST / questions /
    # Update an existing question:         PUT / questions / {id}
    # Update part of an existing question: PATCH / questions / {id}
    # Remove a question:                   DELETE / questions / {id} /


# ROUTER answer ENDPOINTS
    # List all answers:                  GET / answers /
    # Retrieve a specific answer:        GET / answers / {id}
    # Add a new answer:                  POST / answers /
    # Update an existing answer:         PUT / answers / {id}
    # Update part of an existing answer: PATCH / answers / {id}
    # Remove a answer:                   DELETE / answers / {id} /



# # =================================================================================
# # Old patterns without right before going full ModelViewSet Views
# # =================================================================================
# urlpatterns = [
#     # path('', views.api_root),
#     path('admin/', admin.site.urls),
#     path('auth/', include('djoser.urls')),
#     path('auth/', include('djoser.urls.authtoken')),
#     path('api-auth/', include('rest_framework.urls')),
#     path('users/', views.UserList.as_view(), name='user-list'),
    
#     path('question/', views.QuestionViewSet.as_view({'post': 'create'}), name='question-create'),
#     path('questions/', views.QuestionViewSet.as_view({'get': 'list'}), name='questions-list'),
#     # path('questions/', views.ListAllQuestionsView.as_view(), name='question-list'),

#     path('answer/', views.UserAnswerView.as_view(), name='answer-create-get'),
#     path('answers/', views.UserAnswerView.as_view(), name='answer-list'),
#     path('answer/<int:answer_pk>', views.ChangeAnswer.as_view(), name='answer-detail'),
# ]
