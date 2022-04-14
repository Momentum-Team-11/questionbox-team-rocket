from django.contrib import admin
from django.urls import path, include
from questionbox import views
from questionbox.views import AnswerViewSet, QuestionFavoriteView, QuestionViewSet, AnswerDetailView, QuestionDetailView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'favorited', QuestionFavoriteView)
router.register(r'answers', AnswerViewSet)
# router.register(r'answers', AnswerViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', views.UserList.as_view(), name='user-list'),
    # path('favorited/question/', views.QuestionDetailView.as_view(), name='favorited-question'),
    # path('favorited/question/<int:pk>/', views.QuestionDetailView.as_view(), name='favorited-question'),
    # path('favorited/answer/<int:pk>/', views.AnswerDetailView.as_view(), name='favorited-question')
]


