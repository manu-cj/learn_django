from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Inclut tous les champs du modèle


from .models import User  # Importer le modèle User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'birthdate', 'website', 'location', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}  # Assure que le mot de passe est uniquement pour l'écriture
