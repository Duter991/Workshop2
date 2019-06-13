# Workshop2

Django REST Api (DOC: https://www.django-rest-framework.org/)

# Setup

Lancer les commandes :

```bash
sudo dnf -y install python3 python3-pip python3-devel
git clone https://github.com/Duter991/Workshop2.git
cd Workshop2
sudo pip3 install -r requirement.txt
cd server
python3 manage.py migrate
python3 manage.py makemigrations
```

# Sujet

Créer une application Django appelée ``api`` comme ceci:
```bash
python3 manage.py startapp api
```

C'est ici que se trouvera tout le code lié à l'api que vous développerez.

### EX 1

Le premier exercice sera de créer l'url suivant :

http://localhost:8000/api/users/

Ce lien permettra de récupérer un json contenant une liste de tout les usernames des comptes existants.

## EX 2

Une requète sur l'url http://localhost:8000/api/users/?username=MonUsername donnera un json avec les champs suivants :
  - ``name`` : le prénom de l'utilisateur
  - ``last_name`` : le nom de famille de l'utilisateur
  - ``email`` : l'email de l'utilisateur
  
## EX 3

La même requète que l'exercice précédant fera une erreur "403 Permission Denied", il faudra ajouter l'argument ``token`` :

```
http://localhost:8000/api/users/?username=MonUsername -> ERROR
http://localhost:8000/api/users/?username=MonUsername&token=MonToken -> SUCCESS (si le token est associé à l'user MonUsername dans la base de donnée)
```

# Rappels

Pour assigner un lien, il faudra modifier les fichiers ``urls.py`` (``server/urls.py`` et ``api/urls.py``, créer le fichier ``urls.py`` si inexistant).

Le code qui sera executé lors d'une requète se trouvera dans les fichiers ``views.py`` (``api/views.py`` sera le seul fichier à modifier)
