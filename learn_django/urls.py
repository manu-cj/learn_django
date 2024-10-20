"""
URL configuration for learn_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from blog import views  # Importe les vues de l'application blog
from blog.views import PostList, PostDetail 
from blog.views import UserListCreate, UserDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    # path('', views.home),  # Associe l'URL racine à la vue home
    # path('blog/', views.blog_list), # route du blog
    # path('api/posts/', PostList.as_view(), name='post-list'),  # Liste et création des posts
    # path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Détails, mise à jour et suppression d'un post
    # path('api/users/', UserListCreate.as_view(), name='user-list-create'),  # Route pour la liste et la création d'utilisateurs
    # path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # Route pour récupérer, mettre à jour ou supprimer un utilisateur
]

