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
![Screenshot from 2024-11-18 18-59-35](https://github.com/user-attachments/assets/f53e5dfb-cc31-4ae6-a06e-886965475faf)


2. register and login

user can register and login, and can see the posts that user has created.
![Screenshot from 2024-11-18 19-04-25](https://github.com/user-attachments/assets/3a7a82b7-38b3-4263-9ddf-6d4e7414c701)


3. message within the website

user can send message to other users, and can see the messages that user has sent.
![Screenshot from 2024-11-18 19-05-27](https://github.com/user-attachments/assets/88b9d3e5-ed86-45ae-ae6f-097522554797)


