from tokenize import group
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.IntegerField(default=00000000000)

# Create your models here.
