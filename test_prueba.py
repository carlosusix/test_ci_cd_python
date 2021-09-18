from unittest import TestCase
from unittest import TestCase, skip
from prueba import sumatoria

class TestPruebas(TestCase):
    @skip('Demostramdo los test, no sirve este test')
    def prueba(self):
        nombre = 'Eduardo'
        self.asserEqual(nombre, 'eduardo')

    def testSumatoria(self):
        resultado = sumatoria(5,6)
        # self.asserEqual(resultado, 11)
        self.assertNotEqual(resultado, 10)