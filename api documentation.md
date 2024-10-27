# API Documentation

## Table of Contents
1. [Home](#home)
2. [Blog](#blog)
3. [Users](#users)
4. [Posts](#posts)
5. [Employer](#employer)
6. [Projects](#projects)
7. [Tasks](#tasks)
8. [Authentication](#authentication)

---

## Home
### `GET /`
- **Description**: Affiche la page d'accueil de l'API.
- **Response**: Affiche un message de bienvenue ou des informations de base.

---

## Blog
### `GET /blog/`
- **Description**: Récupère la liste des articles de blog.
- **Response**: Retourne un tableau JSON contenant les articles de blog.

---

## Users

### `GET /usershtml/`
- **Description**: Affiche une liste HTML des utilisateurs.
- **Response**: Une page HTML listant les utilisateurs.

### `GET /users/`
- **Description**: Récupère la liste de tous les utilisateurs.
- **Response**: Un tableau JSON des utilisateurs.

### `POST /users/`
- **Description**: Crée un nouvel utilisateur.
- **Body Parameters**:
  - `username` (string, required): Nom d'utilisateur unique.
  - `email` (string, required): Adresse email unique.
  - `password` (string, required): Mot de passe (haché).
- **Response**: Détails de l'utilisateur nouvellement créé.

### `GET /users/<int:pk>/`
- **Description**: Récupère les détails d'un utilisateur spécifique.
- **URL Parameters**:
  - `pk` (int): ID de l'utilisateur.
- **Response**: Détails de l'utilisateur.

---

## Posts

### `GET /posts/`
- **Description**: Récupère la liste des articles de blog.
- **Response**: Tableau JSON contenant les articles de blog.

### `POST /posts/`
- **Description**: Crée un nouvel article.
- **Body Parameters**:
  - `title` (string, required): Titre de l'article.
  - `content` (string, required): Contenu de l'article.
- **Response**: Détails de l'article nouvellement créé.

### `GET /posts/<int:pk>/`
- **Description**: Récupère les détails d'un article spécifique.
- **URL Parameters**:
  - `pk` (int): ID de l'article.
- **Response**: Détails de l'article.

---

## Employer

### `GET /employer/`
- **Description**: Récupère la liste des employeurs.
- **Response**: Tableau JSON contenant les employeurs.

### `POST /employer/`
- **Description**: Crée un nouvel employeur.
- **Body Parameters**:
  - `username` (string, required): Nom d'utilisateur unique.
  - `email` (string, required): Adresse email unique.
  - `password` (string, required): Mot de passe (haché).
- **Response**: Détails de l'employeur nouvellement créé.

### `GET /employer/<int:pk>/`
- **Description**: Récupère les détails d'un employeur spécifique.
- **URL Parameters**:
  - `pk` (int): ID de l'employeur.
- **Response**: Détails de l'employeur.

---

## Projects

### `GET /projects/`
- **Description**: Récupère la liste des projets.
- **Response**: Tableau JSON contenant les projets.

### `POST /projects/`
- **Description**: Crée un nouveau projet.
- **Body Parameters**:
  - `name` (string, required): Nom unique du projet.
  - `description` (string, required): Description du projet.
  - `start_date` (date, required): Date de début du projet.
  - `end_date` (date, optional): Date de fin du projet.
  - `status` (string, optional): Statut du projet (`pending`, `in_progress`, `completed`, `cancelled`).
  - `priority` (string, optional): Priorité du projet (`low`, `medium`, `high`).
- **Response**: Détails du projet nouvellement créé.

### `GET /projects/<int:pk>/`
- **Description**: Récupère les détails d'un projet spécifique.
- **URL Parameters**:
  - `pk` (int): ID du projet.
- **Response**: Détails du projet.

---

## Tasks

### `GET /tasks/`
- **Description**: Récupère la liste des tâches.
- **Response**: Tableau JSON contenant les tâches.

### `POST /tasks/`
- **Description**: Crée une nouvelle tâche.
- **Body Parameters**:
  - `name` (string, required): Nom de la tâche.
  - `description` (string, required): Description de la tâche.
  - `start_date` (date, required): Date de début de la tâche.
  - `end_date` (date, optional): Date de fin de la tâche.
  - `status` (string, optional): Statut de la tâche (`pending`, `in_progress`, `completed`, `cancelled`).
  - `priority` (string, optional): Priorité de la tâche (`low`, `medium`, `high`).
- **Response**: Détails de la tâche nouvellement créée.

### `GET /tasks/<uuid:pk>/`
- **Description**: Récupère les détails d'une tâche spécifique.
- **URL Parameters**:
  - `pk` (UUID): ID de la tâche.
- **Response**: Détails de la tâche.

### `GET /projects/<uuid:project_id>/tasks/`
- **Description**: Récupère les tâches d'un projet spécifique.
- **URL Parameters**:
  - `project_id` (UUID): ID du projet.
- **Response**: Liste des tâches associées au projet.

### `POST /tasks/<uuid:task_id>/duplicate/`
- **Description**: Duplique une tâche spécifique.
- **URL Parameters**:
  - `task_id` (UUID): ID de la tâche à dupliquer.
- **Response**: Détails de la tâche dupliquée.

---

## Authentication

### `POST /register/`
- **Description**: Inscription d'un nouvel utilisateur.
- **Body Parameters**:
  - `username` (string, required): Nom d'utilisateur unique.
  - `email` (string, required): Adresse email unique.
  - `password` (string, required): Mot de passe.
- **Response**: Détails de l'utilisateur nouvellement inscrit.

### `POST /login/`
- **Description**: Authentification de l'utilisateur et obtention du token JWT.
- **Body Parameters**:
  - `username` (string, required): Nom d'utilisateur.
  - `password` (string, required): Mot de passe.
- **Response**: Token d'authentification JWT.

### `POST /token/refresh/`
- **Description**: Rafraîchit le token JWT pour maintenir la session de l'utilisateur.
- **Body Parameters**:
  - `refresh` (string, required): Token de rafraîchissement.
- **Response**: Nouveau token d'authentification JWT.
