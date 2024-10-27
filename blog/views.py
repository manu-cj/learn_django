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

class TaskListByProject(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project_id=project_id)

from datetime import timedelta

class DuplicateTaskView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        task_id = kwargs['task_id']
        task = Task.objects.get(id=task_id)

        # Vérifier que la tâche a bien une date de début et de fin
        if not task.end_date or not task.start_date:
            return Response({"error": "La tâche doit avoir une date de début et de fin."}, status=400)

        # Calculer la durée totale de la tâche
        duration = (task.end_date - task.start_date).days

        # Vérifier que la durée est positive
        if duration <= 0:
            return Response({"error": "La durée de la tâche doit être positive."}, status=400)


        # Créer une nouvelle tâche dupliquée
        duplicated_task = Task(
            project=task.project,
            name=task.name +  " part " + str(task.part + 1),
            description=task.description,
            start_date=task.start_date + timedelta(days=duration // 2),  # Même date de début que la tâche d'origine
            end_date=task.end_date,  # Fin à la moitié de la durée de la tâche d'origine
            status=task.status,
            priority=task.priority,
            part=task.part + 1
        )
        duplicated_task.save()

        # Mettre à jour la tâche d'origine
        task.end_date = task_end_date = task.start_date + timedelta(days=duration // 2)  
        task.part = task.part + 1
        task.save()

        # Sérialiser et retourner la tâche dupliquée
        duplicated_task_serializer = TaskSerializer(duplicated_task)
        return Response(duplicated_task_serializer.data, status=201)

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





