from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from appcore import views
from appcore.admin import admin_site

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
    path('admin/', admin_site.urls),
    path('api/', include(r.urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
