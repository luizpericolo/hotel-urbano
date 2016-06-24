import unittest

from my_math.sum import my_sum

class SumTests(unittest.TestCase):
    def test_zero_sum(self):
        result = my_sum(0, 0)
        self.assertEquals(0, result)

    def test_integer_sum(self):
        result = my_sum(1, 3)
        self.assertEquals(4, result)

    def test_neutral_element_sum(self):
        self.assertEquals(1, my_sum(0, 1))
        self.assertEquals(2, my_sum(0, 2))
        self.assertEquals(3, my_sum(0, 3))



if __name__ == "__main__":
    unittest.main()
