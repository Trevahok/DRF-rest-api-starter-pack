
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comments instances.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer