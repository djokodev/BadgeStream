# Documentation

## Introduction
### Web platform using Django, allowing users to create accounts, upload, and view animated videos, while incorporating a badge system to automatically reward user actions. Technologies used: Django and PostgreSQL ###

## Prerequisites
### 

**1. Python**  : Python is the programming language in which Django is written. You must have a compatible version of Python installed on your system.
    
**2. PostgreSQL** :PostgreSQL is the database management system used in the application. You need PostgreSQL installed on your system

**3. Git** : Git: You will need Git to clone the repository 

###

## Installation

### Installation and Configuration of PostgreSQL Database

1. Installation

Download and install PostgreSQL from https://www.postgresql.org/download/  


2. Create a database, a user, and assign all privileges to the user on the database

```bash
$ CREATE DATABASE nomDeVotreBD;
$ CREATE USER nomDeVotreUtilisateur WITH PASSWORD motDePasseDeVotreUtilisateur;
$ ALL PRIVILEGES ON DATABASE nomDeVotreBD TO nomDeVotreUtilisateur;
```  


3. Clone the project:

Clone the Git repository of the project to your computer.

```bash
$ git clone https://github.com/djokodev/badgeStream.git
```  

    
4. Configure environment variables:

Create a `.env` file at the root of the project, copy the content from `.env.exemple` then paste it into your `.env`  

    
5. Create a virtual environment:

It’s recommended to use a virtual environment to isolate the project dependencies from other Python projects on your system.

```bash
$ cd nom-du-projet 
```

```bash
$ python -m venv nomDeEnvironementVirutuel
```  


6. Activate the virtual environment:

On Windows:
```bash
$ nomDeEnvironementVirutuel\Scripts\activate
```
If using Git Bash:
```bash
source nomDeVotreEnvironmenetViertuel/Scripts/activate
```

On Mac:
```bash
$ source nomDeEnvironementVirutuel/bin/activate 
```

If this command executed without any issues, you should see the name of your virtual environment in your console.


7. Install dependencies: Install the project dependencies from the requirements.txt file. Use the command:
   
```python
pip install -r requirements.txt
```    


8. Apply database migrations: You need to apply the database migrations to create the necessary tables for the application. Run the command:
   
```python
python manage.py migrate
```

## Usage

### Now that you've installed and configured the Django application with PostgreSQL, you can start using it 🙂

1. Create a superuser: To log into the app or access the Django admin interface and manage users, videos, and badges, you need to create a superuser. Run:
    
```python
python manage.py createsuperuser
```  


2. Run the development server: Finally, you can start the Django development server to access the application in a web browser. Run:
    
```python
python manage.py runserver
```  


The application will then be accessible at `http://127.0.0.1:8000/` in your web browser. However, depending on the URL file configuration, the application’s home page may be located at a different address, like `http://127.0.0.1:8000/video/home`

Take a moment to check the URL files of the different apps and discover the available routes.  

happy hacking ✨




