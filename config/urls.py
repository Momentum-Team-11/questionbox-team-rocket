"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from questionbox import views


urlpatterns = [
    path('', views.api_root),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('question/', views.UserQuestionView.as_view(), name='question-create-get'),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('answer/', views.UserAnswerView.as_view(), name='answer-create-get'),
    path('answers/', views.UserAnswerView.as_view(), name='answer-list'),
    path('answer/<int:answer_pk>', views.ChangeAnswer.as_view(), name='answer-detail'),
]
