from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    userEmail = models.EmailField(unique=True)
    dataDeNascimento =models.DateField()
    senhaUser = models.CharField(max_length=500)

    class Meta:
        ordering = ['name']

        