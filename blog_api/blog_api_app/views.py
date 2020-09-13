from .models import Post, Label, Comment, Author
from .serializers import PostSerializer, LabelSerializer, CommentSerializer, AuthorSerializer
from rest_framework import generics


class PostCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LabelCreate(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class CommentCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class AuthorCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
