from django.db import models

# Create your models here.

class Genero(models.Model):
    nome = models.CharField('nome', max_length=100, unique=True)
    descricao = models.TextField('descricao', blank=True, null=True)
    class Meta:
        verbose_name = 'Generos'
        verbose_name_plural = 'Generos'
        ordering =['id']

    def __str__(self):
        return self.nome

