from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appcore import views

r = routers.DefaultRouter()
r.register('users', views.UserViewSet, 'users')
r.register('profiles', views.ProfileViewSet, 'profiles')
r.register('posts', views.PostViewSet, 'posts')
r.register('comments', views.CommentViewSet, 'comments')
r.register('reactions', views.ReactionViewSet, 'reactions')
r.register('surveys', views.SurveyViewSet, 'surveys')
r.register('survey-responses', views.SurveyResponseViewSet, 'survey-responses')
r.register('notifications', views.NotificationViewSet, 'notifications')
r.register('groups', views.GroupViewSet, 'groups')

urlpatterns = [
    path('', include(r.urls))
]
