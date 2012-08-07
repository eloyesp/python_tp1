from ejercicios import base10

import unittest

class TestSequenceFunctions(unittest.TestCase):
    
    def test_cero(self):
        self.assertEqual(base10("0"), 0)

    def test_uno(self):
        self.assertEqual(base10("1"), 1)

    def test_dos(self):
        self.assertEqual(base10("10"), 2)

    def test_diez(self):
        self.assertEqual(base10("1010"), 10)

    def test_grande(self):
        self.assertEqual(base10("1011111"), 95)

    def test_negativo(self):
        self.assertEqual(base10(-1011111), -2)

    def test_error(self):
        self.assertEqual(base10("15"), -1)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

