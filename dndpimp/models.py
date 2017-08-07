from django.db import models

# Create your models here.
class Treasure(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)