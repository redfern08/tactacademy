from rest_framework import generics, viewsets


from users.models import AppUser
from posts.models import Post
from .serializers import UsersSerializer, PostSerializer

class UsersViewset(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UsersSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UsersSerializer

# Next is the posts viewset and RUD API view

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


