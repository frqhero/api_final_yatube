from rest_framework import viewsets
from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
