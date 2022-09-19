from rest_framework import viewsets
from posts.models import Post, Group, Follow, User
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        pk_post = self.kwargs.get('pk_post')
        post = get_object_or_404(Post, pk=pk_post)
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk_post'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        usr = self.request.user
        return Follow.objects.filter(user=usr)

    def perform_create(self, serializer):
    #     # follow_obj = get_object_or_404(User, username=serializer.data['following'])
    #     # serializer.save(user=self.request.user, following=follow_obj)
        serializer.save(user=self.request.user)
