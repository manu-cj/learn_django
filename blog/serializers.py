from rest_framework import serializers
from .models import Post
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Inclut tous les champs du modèle




from .models import User  # Importer le modèle User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] # Inclut tous les champs du modèle
        extra_kwargs = {'password': {'write_only': True}}  # Assure que le mot de passe est uniquement pour l'écriture



from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email','first_name', 'last_name', 'is_superuser', 'is_active', 'date_joined','password']  # Inclut tous les champs du modèle

    def create(self, validated_data):
        # Vérifiez si l'utilisateur existe déjà
        if User.objects.filter(username=validated_data['username']).exists():
            raise ValidationError({"username": "Ce nom d'utilisateur est déjà pris."})

        if User.objects.filter(email=validated_data['email']).exists():
            raise ValidationError({"email": "Cet email est déjà utilisé."})

        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])  # Sécurise le mot de passe
        user.save()
        return user



from .models import Employer # Importer le modèle Employer

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
