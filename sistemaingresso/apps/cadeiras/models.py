from django.db import models

# Create your models here.

class Cadeira(models.Model):

    TIPO_CHOICES = [
        ('NORMAL', 'Normal'),
        ('VIP', 'VIP'),
        ('PCD', 'Pessoa com Deficiência'),
    ]
    fileira = models.CharField(max_length=2)
    numero = models.PositiveIntegerField('numero', unique=True)
    sala = models.PositiveIntegerField(default=1, help_text="Número da sala de cinema.")
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='NORMAL')

    def __str__(self):
        return f"Sala {self.sala} - {self.fileira}{self.numero} ({self.get_tipo_display()})"

    class Meta:
        verbose_name = "Cadeira"
        verbose_name_plural = "Cadeiras"
        unique_together = ('fileira', 'numero', 'sala')