from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('nome', max_length=255) 
    email = models.EmailField('E-mail', unique=True, null=False, blank=False) 
    cpf = models.CharField(max_length=14, unique=True,)  
    telefone = models.CharField('Telefone celular', max_length=20)

class Meta:
        verbose_name = 'Usuarios'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

def __str__(self):
        return self.nome