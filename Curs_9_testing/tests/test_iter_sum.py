import unittest
from functions import iter_sum


class TestIterSum(unittest.TestCase):
    def test_iter_sum(self):
        result = iter_sum([1, 2, 3])
        expected_result = 6

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
