from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    favorite_movies = models.ManyToManyField('movie.Movie')
    avatar = models.ImageField(upload_to="imagees/avatar/")