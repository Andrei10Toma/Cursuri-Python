import unittest
from functions import iterator_sum


class TestIteratorsSum(unittest.TestCase):
    def test_iterator_sum(self):
        results = iterator_sum([1, 2, 3], [4, 5], 'abc')
        expected_results = [6, 9, 0]

        self.assertEqual(results, expected_results)


if __name__ == '__main__':
    unittest.main()
