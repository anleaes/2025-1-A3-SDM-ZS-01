from django.db import models
from usuarios.models import Usuario


# Create your models here.

class Compra(models.Model):
    
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADA', 'Aprovada'),
        ('CANCELADA', 'Cancelada'),
    ]
    PAGAMENTO_CHOICES = [
        ('CREDITO', 'Cartão de Crédito'),
        ('DEBITO', 'Cartão de Débito'),
        ('PIX', 'PIX'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="compras") # 
    data = models.DateTimeField('data', auto_now_add=True) # 
    valor_total = models.DecimalField('valor total', max_digits=10, decimal_places=2, default=0.00) # 
    status = models.CharField('satatus', max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    metodo_pagamento = models.CharField('metodo de pagamento',max_length=20, choices=PAGAMENTO_CHOICES, blank=True, null=True)

    
class Meta:
    verbose_name = "Compra"
    verbose_name_plural = "Compras"
    ordering = ['-data']
    
def __str__(self):
    return f"Compra {self.id} de {self.usuario.nome} - Status: {self.get_status_display()}"
