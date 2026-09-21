from django.db import models
from django.contrib.auth.models import AbstractUser
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    selecao = models.ForeignKey(Selecao, on_delete=models.PROTECT)
class Selecao(models.Model):
    nome = models.CharField(max_length=100)
# Create your models here.
