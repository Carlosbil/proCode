import unittest
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from array_strings.merge_strings_alternately import Solution, Solution2
# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.mergeAlternately("abc", "pqr"), "apbqcr")

    def test_case_2(self):
        self.assertEqual(self.solution.mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_case_3(self):
        self.assertEqual(self.solution.mergeAlternately("abcd", "pq"), "apbqcd")

    def test_case_4(self):
        self.assertEqual(self.solution.mergeAlternately("", "xyz"), "xyz")

    def test_case_5(self):
        self.assertEqual(self.solution.mergeAlternately("abcd", ""), "abcd")

class TestSolution2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test_case_1(self):
        self.assertEqual(self.solution.mergeAlternately("abc", "pqr"), "apbqcr")

    def test_case_2(self):
        self.assertEqual(self.solution.mergeAlternately("ab", "pqrs"), "apbqrs")

    def test_case_3(self):
        self.assertEqual(self.solution.mergeAlternately("abcd", "pq"), "apbqcd")

    def test_case_4(self):
        self.assertEqual(self.solution.mergeAlternately("", "xyz"), "xyz")

    def test_case_5(self):
        self.assertEqual(self.solution.mergeAlternately("abcd", ""), "abcd")

# Measure execution time for unit tests
def run_tests():
    for test_class in [TestSolution, TestSolution2]:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        start_time = time.time()
        unittest.TextTestRunner().run(suite)
        end_time = time.time()
        print(f"{test_class.__name__} execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_tests()
    
"""
Results:

PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution execution time: 0.0010 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0000 seconds
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution execution time: 0.0000 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0010 seconds
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
TestSolution execution time: 0.0010 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0000 seconds
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution execution time: 0.0000 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0010 seconds
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution execution time: 0.0010 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0010 seconds
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution execution time: 0.0000 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0010 seconds
PS E:\proCode> & C:/Python311/python.exe e:/proCode/python_problems/array_strings_tests/1768_merge_strings_alternately.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution execution time: 0.0010 seconds
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
TestSolution2 execution time: 0.0010 seconds
"""