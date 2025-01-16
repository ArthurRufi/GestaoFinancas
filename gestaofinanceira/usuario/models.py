from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    userEmail = models.EmailField()
    dataDeNascimento =models.DateField()
    senhaUser = models.CharField()

    class Meta:
        ordering = ['name']

        