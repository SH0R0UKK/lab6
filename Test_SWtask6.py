
import unittest
from SWtask6 import addnum

class Test_SWtask6(unittest.TestCase):
    def test_addnum(self):
        result = addnum(5, 5)
        self.assertEqual(result, 10)

        # Test addition of two negative numbers
        result = addnum(-5, -3)
        self.assertEqual(result, -8)

        # Test addition of a positive and a negative number
        result = addnum(5, -1)
        self.assertEqual(result, 4)

        # Test addition with zero and a positive number
        result = addnum(0, 8)
        self.assertEqual(result, 8 )

        # Test addition with zero and a negative number
        result = addnum(0, -20)
        self.assertEqual(result, -20)

        # Test addition of large numbers
        result = addnum(1000000, 2000000)
        self.assertEqual(result, 3000000)

        # Test addition of small floating-point numbers
        result = addnum(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=1)

if __name__ == '__main__':
    unittest.main()
