import unittest
from typing import List
from python_problems.array_strings.increase_triplet_subsequence import Solution

class TestIncreasingTriplet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.increasingTriplet([1, 2, 3, 4, 5]))

    def test_example_2(self):
        self.assertFalse(self.solution.increasingTriplet([5, 4, 3, 2, 1]))

    def test_example_3(self):
        self.assertTrue(self.solution.increasingTriplet([2, 1, 5, 0, 4, 6]))

    def test_no_triplet(self):
        self.assertFalse(self.solution.increasingTriplet([10, 9, 8, 1, 2]))

    def test_triplet_at_end(self):
        self.assertTrue(self.solution.increasingTriplet([10, 1, 5, 3, 4, 6]))

    def test_negative_numbers(self):
        self.assertTrue(self.solution.increasingTriplet([-3, -2, -1, 0, 1]))

    def test_with_duplicates(self):
        self.assertTrue(self.solution.increasingTriplet([2, 2, 3, 1, 4]))

    def test_short_array(self):
        self.assertFalse(self.solution.increasingTriplet([1, 2]))  # Not enough elements

    def test_long_increasing_sequence(self):
        self.assertTrue(self.solution.increasingTriplet(list(range(100))))

    def test_decreasing_then_increasing(self):
        self.assertTrue(self.solution.increasingTriplet([10, 9, 2, 3, 5]))

    def test_large_numbers(self):
        self.assertTrue(self.solution.increasingTriplet([1000000, 2000000, 3000000]))

    def test_boundary_values(self):
        self.assertFalse(self.solution.increasingTriplet([float('inf'), float('inf'), float('inf')]))

def run_tests():
    unittest.main()

if __name__ == '__main__':
    run_tests()