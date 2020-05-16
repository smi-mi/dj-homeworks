from django.contrib.auth.models import User, AbstractUser
from django.db import models


class ArticleUser(AbstractUser):
    did_pay = models.BooleanField(default=False)


class Profile(models.Model):
    pass


class Article(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    is_paid = models.BooleanField(default=False)
