from django.http import HttpResponse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny

from .models import User

def home(request):
        return HttpResponse("Hello, Django !")


from django.shortcuts import render
from .models import Post  # Importe le modèle Post

def blog_list(request):
    posts = Post.objects.all()  # Récupère tous les articles
    
    return render(request, 'blog_list.html', {'posts': posts})  # Passe les articles au template

def users_list(request):
    users = User.objects.all()
    
    return render(request, 'users_list.html', {'users': users})


from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes = [JWTAuthentication]  # Authentification par JWT
    # permission_classes = [IsAuthenticated]  # Seulement les utilisateurs authentifiés peuvent accéder à cette vue


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()  # Récupère tous les articles
    serializer_class = PostSerializer  # Utilise le serializer pour la réponse

# Employer

from .models import Employer
from .serializers import EmployerSerializer
class EmployerList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer


# User
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Project

from .models import Project
from.serializers import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Task

from .models import Task
from.serializers import TaskSerializer

class TaskList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# Vue pour l'inscription
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vue pour obtenir le token JWT lors de la connexion
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajouter des claims personnalisés (facultatif)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





