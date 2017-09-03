from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Party(models.Model):
    class Meta:
        verbose_name_plural = "parties"
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
