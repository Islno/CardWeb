import locale
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.nome
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15,verbose_name="C.P.F")
    datanasc = models.DateField(verbose_name="Data de Nascimento")


    def __str__(self):
        return self.nome
    
    @property
    def datanascimento(self):
        """Retorna a data de nascimento no formato DD/MM/AAAA"""
        if self.datanasc:
            return self.datanasc.strftime('%d/%m/%Y')
        return None