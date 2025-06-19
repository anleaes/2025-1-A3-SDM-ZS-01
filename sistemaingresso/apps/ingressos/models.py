from django.db import models
from sessoes.models import Sessao
from cadeiras.models import Cadeira


# Create your models here.

class Ingresso(models.Model):
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE, related_name="ingressos") 
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE, related_name="ingressos")
    preco = models.DecimalField(max_digits=8, decimal_places=2) 

    def __str__(self):
        return f"Ingresso para {self.sessao.filme.titulo} - {self.cadeira}"

    class Meta:
        verbose_name = "Ingresso"
        verbose_name_plural = "Ingressos"
        unique_together = ('sessao', 'cadeira')