from django.db import models

# Create your models here.


class User(models.Model):

    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField()

    birthdate = models.DateField(blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


