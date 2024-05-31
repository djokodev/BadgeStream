# Documentation

## Introduction 
### plateforme web utilisant Django permettant aux utilisateurs de créer des comptes, de télécharger et de visualiser des vidéos animées,  tout en intégrant un système de badges pour récompenser les actions des utilisateurs de facon automatique. Technologies utilisées : Django et PostgreSQL ###

## Prérequis
### 
**1. Python**  : Python est le langage de programmation dans lequel Django est écrit. Vous devez avoir une version compatible de Python installée sur votre système. Vous pouvez télécharger Python à partir du site   
    officiel : https://www.python.org/downloads/
    
**2. PostgreSQL** : PostgreSQL est le système de gestion de base de données utilisé dans l'application. Vous devez avoir PostgreSQL installé sur votre système. Vous pouvez télécharger PostgreSQL à partir du site officiel : https://www.postgresql.org/download/  

**3. Git** : Vous devez avoir besoin de Git pour cloner le dépôt. Vous pouvez télécharger Git à partir du site officiel : https://git-scm.com/downloads
###

## Instalation
### 
  - Configuration de postgreSQL : Créer une base de données PostgreSQL, Pour ce faire, vous pouvez utiliser l'interface graphique pgAdmin ou la ligne de commande psql. Voici un exemple de création de base de données à 
    l'aide de psql : `CREATE DATABASE nomDeVotreBD;`
    
  - Créer un utilisateur PostgreSQL : Vous devez créer un utilisateur PostgreSQL pour se connecter à la base de données. Pour ce faire, vous pouvez utiliser l'interface graphique pgAdmin ou la ligne de commande psql.         Voici un exemple de création d'utilisateur à l'aide de psql : `CREATE USER nomDeVotreUtilisateur WITH PASSWORD motDePasseDeVotreUtilisateur;`
    
  - Accorder des privilèges à l'utilisateur que vous avez créé : Vous devez accorder des privilèges à nomDeVotreUtilisateur pour qu'il puisse accéder à la base de données. Pour ce faire, vous pouvez
    utiliser l'interface graphique pgAdmin ou la ligne de commande psql. Voici un exemple d'octroi de privilèges à l'aide de psql : `GRANT ALL PRIVILEGES ON DATABASE nomDeVotreBD TO nomDeVotreUtilisateur;`
    
  - Cloner le projet : Cloner le dépôt Git du projet sur votre ordinateur. Pour ce faire, vous pouvez utiliser la commande `git clone https://github.com/djokodev/badgeStream.git`
    
  - Configurer les variables d'environnement : Vous devez configurer les variables d'environnement pour que votre application Django puisse se connecter à la base de données PostgreSQL. Pour ce faire, vous devez créer un 
    fichier `.env` à la racine de votre projet (au même niveau que manage.py) et y ajouter les informations suivantes : 
    `DB_NAME=nomDeVotreBD`
    `DB_USER=nomDeVotreUtilisateur`
    `DB_PASSWORD=motDePasseDeVotreUtilisateur`
    `DB_HOST=localhost`
    `DB_PORT=5432`
    
  - Créer un environnement virtuel : Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de votre projet des autres projets Python sur votre système. Pour créer un environnement virtuel, les 
    utilisateurs peuvent utiliser la commande **python -m venv suivie du nom de l'environnement**. Par exemple : naviguer dans le dossier du projet, pour les utilisateurs de **Windows** : `cd votre-projet` , pour ceux de 
    macOS et Linux `cd votre-projet/` exécuteur ensuite `python -m venv nomDeVotreEnvironmenetViertuel` pour créer votre environnement virtuel

  - Activer l'environnement virtuel : vous devez activer l'environnement virtuel pour pouvoir installer les dépendances et exécuter le projet. Pour activer l'environnement virtuel, Sur Windows `env\Scripts\activate` ou       si vous utiliser un terminal git bash utiliser la commande `source nomDeVotreEnvironmenetViertuel/Scripts/activate`, si cette commande c'est executer sans probleme vous devrier voir le nom de votre environement 
    virtuel dans votre console

  - Installer les dépendances : Installer les dépendances du projet à partir du fichier requirements.txt. Pour ce faire utilisez la commande `pip install -r requirements.txt`
###





