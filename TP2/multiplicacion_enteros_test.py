from ejercicios import multiplicacion_enteros

import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test_cero(self):
        self.assertEqual(multiplicacion_enteros(0, 0), 0)
        self.assertEqual(multiplicacion_enteros(0, 12), 0)
        self.assertEqual(multiplicacion_enteros(12, 0), 0)

    def test_uno(self):
        self.assertEqual(multiplicacion_enteros(1, 1), 1)

    def test_positivos(self):
        self.assertEqual(multiplicacion_enteros(5, 3), 15)

    def test_mezcla(self):
        self.assertEqual(multiplicacion_enteros(-5, 3), -15)
        self.assertEqual(multiplicacion_enteros(5, -3), -15)

    def test_negativos(self):
        self.assertEqual(multiplicacion_enteros(-5, -3), 15)

    def test_grandes(self):
        self.assertEqual(multiplicacion_enteros(999999, 15), 15*999999)
        self.assertEqual(multiplicacion_enteros(15, 999999), 15*999999)
        self.assertEqual(multiplicacion_enteros(999999, 999999), 999999*999999)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
