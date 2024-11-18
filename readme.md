# This is a simple template for social media website built with django.

## how to use

This project is a template and not production ready.

To start this project

1. Please make sure your python version is above 3.12

```bash
python -V
```

2. create a virtual environment

```bash
python -m venv venv
```

3. activate the virtual environment

```bash
source venv/bin/activate
```

4. install requirements

```bash
pip install -r requirements.txt
```

5. makemigrations and migrate

```bash
cd social
python manage.py makemigrations
python manage.py migrate
```

6. run test server
    
 ```bash
python manage.py runserver
```

## Main features
1. Add new post and edit post

user can add new post and edit post, with one picture and one YouTube link.

2. register and login

user can register and login, and can see the posts that user has created.

3. message within the website

user can send message to other users, and can see the messages that user has sent.