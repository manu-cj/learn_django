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
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création automatique

    def __str__(self):
        return self.username  # Retourne le nom d'utilisateur

class Employer(models.Model):
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

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Nullable for ongoing projects
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
