import locale
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.nome