import unittest
from mesfonctions import addition, soustraction, multiplication, division, est_pair


class TestMesFonctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_soustraction(self):
        self.assertEqual(soustraction(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 5), 15)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_est_pair(self):
        self.assertTrue(est_pair(4))
        self.assertFalse(est_pair(5))


if __name__ == "__main__":
    unittest.main()