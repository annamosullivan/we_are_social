from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer


class PostUpdateView(generics.UpdateAPIView):

    serializer_class = PostSerializer
    queryset = Posts.objects.all()


class PostDeleteView(generics.DestroyAPIView):

    serializer_class = PostSerializer
    queryset = Posts.objects.all()
