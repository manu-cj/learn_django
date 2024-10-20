from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Titre de l'article
    content = models.TextField()  # Contenu de l'article
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return self.title  # Retourne le titre de l'article en tant que chaîne


from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Nom d'utilisateur unique
    email = models.EmailField(unique=True)  # Adresse email unique
    password = models.CharField(max_length=128)  # Mot de passe (haché)
    bio = models.TextField(blank=True, null=True)  # Biographie de l'utilisateur
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Photo de profil
    birthdate = models.DateField(blank=True, null=True)  # Date de naissance
    website = models.URLField(blank=True, null=True)  # Site web de l'utilisateur
    location = models.CharField(max_length=100, blank=True, null=True)  # Lieu de résidence
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return self.username  # Retourne le nom d'utilisateur
