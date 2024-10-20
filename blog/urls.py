from django.urls import path
from blog import views  # Importe les vues de l'application blog
from blog.views import PostList, PostDetail 
from blog.views import UserListCreate, UserDetail

urlpatterns = [
    path('', views.home),  # Associe l'URL racine à la vue home
    path('blog/', views.blog_list), # route du blog
    path('posts/', PostList.as_view(), name='post-list'),  # Liste et création des posts
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),  # Détails, mise à jour et suppression d'un post
    path('users/', UserListCreate.as_view(), name='user-list-create'),  # Route pour la liste et la création d'utilisateurs
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),  # Route pour récupérer, mettre à jour ou supprimer un utilisateur
]