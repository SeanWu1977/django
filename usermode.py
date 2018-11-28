# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
#Extending User Model Using a Custom Model Extending AbstractUser

# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
# settings.py

AUTH_USER_MODEL = 'usblog.User'  # <<appname>>.User


# python manage.py makemigrations usblog
# python manage.py migrate usblog
