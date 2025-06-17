from django.db import models
from .models import Filme
# Create your models here.

class Sessao(models.Model):
    """
    Representa uma exibição de um filme em um horário e sala específicos.
    """
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name="sessoes") 
    sala = models.PositiveIntegerField('sala')
    horario = models.DateTimeField('horario', help_text="Data e hora de início da sessão.") 
    is_active = models.BooleanField('ativo',default=True)  

    def __str__(self):
        return f"{self.filme.titulo} - Sala {self.sala} ({self.horario.strftime('%d/%m/%Y %H:%M')})"

    class Meta:
        verbose_name = "Sessao"
        verbose_name_plural = "Sessoes"