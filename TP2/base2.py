def base2(n):
    if n == 0:
        resultado = "0"
    elif n == 1:
        resultado = "1"
    elif n > 1:
        resultado = base2(n / 2) + str(n % 2)
    else:
        resultado = "-" + base2(-n)
    return resultado

import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test_cero(self):
        self.assertEqual(base2(0), "0")

    def test_uno(self):
        self.assertEqual(base2(1), "1")

    def test_dos(self):
        self.assertEqual(base2(2), "10")

    def test_diez(self):
        self.assertEqual(base2(10), "1010")

    def test_grande(self):
        self.assertEqual(base2(95), "1011111")

    def test_negativo(self):
        self.assertEqual(base2(-95), "-1011111")
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
