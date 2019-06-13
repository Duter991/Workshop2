# Workshop2

Django REST Api (DOC: https://www.django-rest-framework.org/)

# Setup

Lancés les commandes:

```bash
dnf -y install python3 python3-pip python3-devel
git clone https://github.com/Duter991/Workshop2.git
cd Workshop2
[sudo] pip3 install -r requirement.txt
python3 manage.py migrate
python3 manage.py makemigrations
```

# Sujet

Créé une application Django appelé ``api`` comme ceci:
```bash
python3 manage.py startapp api
```

C'est ici que ce trouveras tout le code lié à l'api que vous développerez.

### EX 1

Le premier exercice seras de créé l'url suivant:

http://localhost:8000/api/users/

Ce liens permettras de récupérer un json contenant une liste de tout les usernames des comptes existants.

## EX 2

Une requéte sur l'url http://localhost:8000/api/users/?username=MonUsername donneras un json avec les champs:
  - ``name``: le prénom de l'utilisateur
  - ``last_name``: le nom de famille de l'utilisateur
  - ``email``: l'email de l'utilisateur
  
## EX 3

La même requete que l'exercice précédant feras une erreur "403 Permission Denied", il faudras rajouté l'argument ``token``:

```
http://localhost:8000/api/users/?username=MonUsername -> ERROR
http://localhost:8000/api/users/?username=MonUsername&token=MonToken -> SUCCESS (si le token est associé à l'user MonUsername dans la base de donnée)
```

# Rappels

Pour assigné un lien, il faudras modifier les fichiers ``urls.py`` (``server/urls.py`` et ``api/urls.py``, créé les fichiers ``urls.py`` si inexistants).

Le code qui seras executer lors d'une requéte ce trouveras dans les fichiers ``views.py`` (``api/views.py`` seras le seul fichier à modifier)
