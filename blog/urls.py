from django.urls import path
from blog import views  # Importe les vues de l'application blog
from .views import (
    users_list, 
    RegisterView, 
    MyTokenObtainPairView,
    EmployerList, 
    EmployerDetail, 
    ProjectList, 
    ProjectDetail, 
    TaskList, 
    TaskDetail,
    TaskListByProject,
    DuplicateTaskView,
)
from blog.views import PostList, PostDetail, UserListCreate, UserDetail
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),

    # Blog
    path('blog/', views.blog_list, name='blog-list'),

    # Utilisateurs
    path('usershtml/', users_list, name='users-html'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # Posts
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),

    # Employer
    path('employer/', EmployerList.as_view(), name='employer-list'),
    path('employer/<int:pk>/', EmployerDetail.as_view(), name='employer-detail'),

    # Projets
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),

    # Tâches
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<uuid:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('projects/<uuid:project_id>/tasks/', TaskListByProject.as_view(), name='tasks-by-project'),
    path('tasks/<uuid:task_id>/duplicate/', DuplicateTaskView.as_view(), name='duplicate-task'),


    # Authentification
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
