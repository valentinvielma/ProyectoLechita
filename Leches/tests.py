from django.test import TestCase
from .models import Leche


# Create your tests here.
class LecheTest(TestCase):

    def SetupTestData(cls):
        # Crea todos los datos no modificables para testear
        Leche.objects.create(Nombre='Lechita', FechaVencimiento='20/12/2020', Cantidad=1, LoteProducto='ABC123')

    def Test_Nombre_Leche(self):
        lechita = Leche.objects.get(Nombre='Lechita')
        self.assertEqual(lechita.Nombre, 'Lechita')

    def Test_Nombre_Malo(self):
        lechita = Leche.objects.get(Nombre='Lechita')
        self.assertEqual(lechita.Nombre, 'Lechota')

    def Test_cantidad_Mayor_Cero(self):
        lechita = Leche.objects.get(Nombre='Lechita')
        self.assertTrue(lechita.Cantidad>0)

