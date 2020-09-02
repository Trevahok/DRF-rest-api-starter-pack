
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters


class PostFilter(filters.FilterSet):
    search = filters.NumberFilter(field_name="title", lookup_expr='in')
    class Meta:
        model = Post
        fields  = [ 'title' , 'text']


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comments instances.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = '__all__'