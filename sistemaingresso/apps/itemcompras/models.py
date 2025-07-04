from django.db import models
from compras.models import Compra
from ingressos.models import Ingresso


# Create your models here.

class Itemcompra(models.Model):
    quantitade = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    preco_unitario = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE, null=True, blank=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('compra', 'ingresso')
        verbose_name = 'Item de pedido'
        verbose_name_plural = 'Itens de pedido'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity} - {self.ingresso.name}"