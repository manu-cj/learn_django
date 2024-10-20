from django.http import HttpResponse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

def home(request):
    return HttpResponse("Hello, Django !")


from django.shortcuts import render
from .models import Post  # Importe le modèle Post

def blog_list(request):
    posts = Post.objects.all()  # Récupère tous les articles
    return render(request, 'blog_list.html', {'posts': posts})  # Passe les articles au template




class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()  # Récupère tous les articles
    serializer_class = PostSerializer  # Utilise le serializer pour la réponse

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()  # Récupère tous les articles
    serializer_class = PostSerializer  # Utilise le serializer pour la réponse


from .models import User
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer