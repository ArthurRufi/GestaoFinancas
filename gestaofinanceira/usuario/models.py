from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    name = models.CharField(max_length=255)
    userEmail = models.EmailField(unique=True)
    dataDeNascimento = models.DateField()
    senhaUser = models.CharField(max_length=500)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        # Criptografar a senha antes de salvar no banco
        if not self.senhaUser.startswith('pbkdf2_sha256$'):  # Evita recriptografar senhas já salvas
            self.senhaUser = make_password(self.senhaUser)
        super().save(*args, **kwargs)

    def verificar_senha(self, senha):
        # Verifica se a senha inserida está correta
        return check_password(senha, self.senhaUser)