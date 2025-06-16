from django.db import models
from generos.models import Genero


# Create your models here.

class Filme(models.Model):
    titulo = models.CharField('titulo', max_length=255)  
    diretor = models.CharField('diretor', max_length=255)  
    data_lancamento = models.DateField('descricao', blank=True, null=True)  
    descricao = models.TextField()
    duracao = models.DurationField()
    generos = models.ManyToManyField(Genero, related_name="filmes")

class Meta:
    verbose_name = "Filme"
    verbose_name_plural = "Filmes"
         
def __str__(self):
    return self.titulo