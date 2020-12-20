import equation as eq 

import unittest 

class TestEquation(unittest.TestCase):
    def test_linear(self):
        self.assertEqual(eq.linear(10,2), 1)
        self.assertEqual(eq.linear(10, 0), 1)
        self.assertEqual(eq.linear(0, 10), 0) 

    def test_quadratic(self):
        self.assertEqual(eq.quadratic(1, 10000, 2), 2)
        self.assertEqual(eq.quadratic(3, 4, 5), 0)
        self.assertEqual(eq.quadratic(1, -4, 4), 1)
        self.assertEqual(eq.quadratic(10, 0, 0), 1) 

    def test_solve(self):
        self.assertEqual(eq.solve([0, 10, 2]), 1) 
        self.assertEqual(eq.solve([0, 10, 0]), 1)
        self.assertEqual(eq.solve([0, 0, 10]), 0)
        self.assertEqual(eq.solve([1, 10000, 2]), 2)
        self.assertEqual(eq.solve([3,4,5]), 0)


if __name__ == "__main__":
    unittest.main()