import unittest

from main import XetaSimulation

class TestSimulation(unittest.TestCase):
    xs = XetaSimulation()

    def test_create_xons(self):
        self.xs.xeta_balance = 20.1

        self.xs.create_xons()
        self.assertEqual(2, len(self.xs.xons))
        self.assertEqual(0.1, round(self.xs.xeta_balance, 6))


if __name__ == '__main__':
    unittest.main()