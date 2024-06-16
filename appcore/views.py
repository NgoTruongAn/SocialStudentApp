from rest_framework import viewsets, generics
from appcore.models import User,Profile, Post, Comment, Reaction, Survey, SurveyResponse, Notification, Group
from appcore import serializers, paginators


class UserViewSet(viewsets.ModelViewSet,generics.CreateAPIView ):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet, generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


class PostViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    queryset = Post.objects.filter(active=True)
    serializer_class = serializers.PostSerializer
    pagination_class = paginators.PostPaginator


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = serializers.ReactionSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = serializers.SurveySerializer


class SurveyResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = serializers.SurveyResponseSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = serializers.NotificationSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
