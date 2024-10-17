import unittest
from python_problems.array_strings.kids_with_the_greatest_number_of_candies import Solution



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        candies = [2, 3, 5, 1, 3]
        extraCandies = 3
        expected = [True, True, True, False, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_example_2(self):
        candies = [4, 2, 1, 1, 2]
        extraCandies = 1
        expected = [True, False, False, False, False]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_example_3(self):
        candies = [12, 1, 12]
        extraCandies = 10
        expected = [True, False, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_all_equal(self):
        candies = [5, 5, 5, 5]
        extraCandies = 3
        expected = [True, True, True, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_no_extra_candies(self):
        candies = [1, 2, 3, 4]
        extraCandies = 0
        expected = [False, False, False, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_large_numbers(self):
        candies = [1000, 2000, 3000, 4000]
        extraCandies = 500
        expected = [False, False, False, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_single_kid(self):
        candies = [10]
        extraCandies = 5
        expected = [True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_two_kids(self):
        candies = [1, 2]
        extraCandies = 1
        expected = [True, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_extra_candies_greater_than_all(self):
        candies = [1, 2, 3]
        extraCandies = 10
        expected = [True, True, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

    def test_extra_candies_equal_to_max(self):
        candies = [1, 2, 3]
        extraCandies = 3
        expected = [True, True, True]
        self.assertEqual(self.solution.kidsWithCandies(candies, extraCandies), expected)

if __name__ == '__main__':
    unittest.main()
    
"""
Results
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/test_array_strings/1431_kids_with_the_greatest_number_of_candies_test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/test_array_strings/1431_kids_with_the_greatest_number_of_candies_test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/test_array_strings/1431_kids_with_the_greatest_number_of_candies_test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/test_array_strings/1431_kids_with_the_greatest_number_of_candies_test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/test_array_strings/1431_kids_with_the_greatest_number_of_candies_test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
"""