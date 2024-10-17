import unittest
from python_problems.array_strings.can_place_flowers import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        expected = True
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_example_2(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        expected = False
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_no_flowers(self):
        flowerbed = [0, 0, 0, 0, 0]
        n = 3
        expected = True
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_all_flowers(self):
        flowerbed = [1, 1, 1, 1, 1]
        n = 1
        expected = False
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_single_plot_empty(self):
        flowerbed = [0]
        n = 1
        expected = True
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_single_plot_not_empty(self):
        flowerbed = [1]
        n = 1
        expected = False
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_adjacent_empty_plots(self):
        flowerbed = [0, 0, 1, 0, 0]
        n = 2
        expected = True
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_large_flowerbed(self):
        flowerbed = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
        n = 3
        expected = True
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_no_new_flowers_needed(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 0
        expected = True
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

    def test_not_enough_space(self):
        flowerbed = [0, 0, 1, 0, 0]
        n = 3
        expected = False
        self.assertEqual(self.solution.canPlaceFlowers(flowerbed, n), expected)

if __name__ == '__main__':
    unittest.main()