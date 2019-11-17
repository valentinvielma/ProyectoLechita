from django.db import models


# Create your models here.

class Leche(models.Model):
    Nombre = models.CharField(max_length=100)
    FechaVencimiento = models.DateField()
    Cantidad = models.IntegerField()
    LoteProducto = models.CharField(max_length=20)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Cantidad)


