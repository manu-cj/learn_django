import uuid
from django.db import models
from django.core.exceptions import ValidationError

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)  # Titre de l'article
    content = models.TextField()  # Contenu de l'article
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return self.title  # Retourne le titre de l'article en tant que chaîne


from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)  # Nom d'utilisateur unique
    email = models.EmailField(unique=True)  # Adresse email unique
    password = models.CharField(max_length=128)  # Mot de passe (haché)
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return self.username  # Retourne le nom d'utilisateur

class Employer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)  # Adresse email unique
    password = models.CharField(max_length=128)  # Mot de passe (haché)
    
    def __str__(self):
        return self.username
    

class Project(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Nullable for ongoing projects
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Vérifiez que start_date n'est pas supérieure à end_date
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("La date de début ne peut pas être supérieure à la date de fin.")

    def save(self, *args, **kwargs):
        # Appel de clean avant de sauvegarder
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Task(models.Model):  # Renommé Tasks -> Task pour respecter les conventions de nommage
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Vérifiez que start_date n'est pas supérieure à end_date
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("La date de début ne peut pas être supérieure à la date de fin.")

    def save(self, *args, **kwargs):
        # Appel de clean avant de sauvegarder
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name