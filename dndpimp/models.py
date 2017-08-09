from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)

class Character(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)
	user = models.OneToOneField(User, blank=True, null=True)