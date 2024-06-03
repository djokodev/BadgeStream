# Documentation

## Introduction 
### plateforme web utilisant Django permettant aux utilisateurs de créer des comptes, de télécharger et de visualiser des vidéos animées,  tout en intégrant un système de badges pour récompenser les actions des utilisateurs de facon automatique. Technologies utilisées : Django et PostgreSQL ###

## Prérequis
### 

**1. Python**  : Python est le langage de programmation dans lequel Django est écrit. Vous devez avoir une version compatible de Python installée sur votre système. 
    
**2. PostgreSQL** : PostgreSQL est le système de gestion de base de données utilisé dans l'application. Vous devez avoir PostgreSQL installé sur votre système.

**3. Git** : Vous devez avoir besoin de Git pour cloner le dépôt. 

###

## Instalation

### Instalation et Configuration de BD PostgreSQL

1. Installation

Telecharger et installer postgreSQL https://www.postgresql.org/download/

2. Créer une base de données, un utilisateur et lui attribuer tous les droits sur la base de données

```bash
$ CREATE DATABASE nomDeVotreBD;
$ CREATE USER nomDeVotreUtilisateur WITH PASSWORD motDePasseDeVotreUtilisateur;
$ ALL PRIVILEGES ON DATABASE nomDeVotreBD TO nomDeVotreUtilisateur;
```

3. Cloner le projet :

Cloner le dépôt Git du projet sur votre ordinateur.

```bash
$ git clone https://github.com/djokodev/badgeStream.git
```
    
4. Configurer les variables d'environnement:

Cree un fichier `.env` a la racine du projet et copier le contenu du fichier `.env.exemple` ensuite coller a votre `.env`
    
5. Créer un environnement virtuel:

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de votre projet des autres projets Python sur votre système.

```bash
$ cd nom-du-projet 
```

```bash
python -m venv nomDeEnvironementVirutuel
```

  - **Activer l'environnement virtuel** : vous devez activer l'environnement virtuel pour pouvoir installer les dépendances et exécuter le projet. Pour activer l'environnement virtuel, Sur Windows `env\Scripts\activate` ou  si vous utiliser un terminal git bash utiliser la commande
     `source nomDeVotreEnvironmenetViertuel/Scripts/activate`, si cette commande c'est executer sans probleme vous devrier voir le nom de votre environement 
    virtuel dans votre console

  - **Installer les dépendances** : Installer les dépendances du projet à partir du fichier requirements.txt. Pour ce faire utilisez la commande `pip install -r requirements.txt`

  - **Appliquer les migrations de la base de données** : vous devez appliquer les migrations de la base de données pour créer les tables nécessaires à l'application. Pour ce faire, exécuter la commande `python manage.py migrate`

## Utilisation 
###
## Maintenant que vous avez installé et configuré l'application Django avec PostgreSQL, vous pouvez commencer à l'utiliser 🙂  
  - **Création d'un superutilisateur** : Pour se connecter a l'application ou accéder à l'interface d'administration de Django et gérer les utilisateurs, les vidéos et les badges, vous devez créer un superutilisateur. Pour ce faire, exécutez `python manage.py createsuperuser`

  - **Exécuter le serveur de développement** : Enfin, vous pouvez exécuter le serveur de développement de Django pour pouvoir accéder à l'application dans un navigateur web. Pour ce faire, exécuter `python manage.py runserver` L'application sera alors accessible à l'adresse
     http://127.0.0.1:8000/ dans votre navigateur web. Cependant, selon la configuration des fichiers URL, la page d'accueil de l'application peut se trouver à une adresse différente `http://127.0.0.1:8000/video/home`
###




