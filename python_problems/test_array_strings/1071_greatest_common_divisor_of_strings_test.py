import unittest
import time
from python_problems.array_strings.greatest_common_divisor_of_strings import *

# Unit tests
class TestGcdOfStrings(unittest.TestCase):
    def setUp(self):
        self.gcdOfStrings = Solution()
    def test_case_1(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABCABC", "ABC"), "ABC")

    def test_case_2(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABABAB", "ABAB"), "AB")

    def test_case_3(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("LEET", "CODE"), "")

    def test_case_4(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("A", "A"), "A")

    def test_case_5(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("AAAA", "AA"), "AA")

    def test_case_6(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABCDEF", "ABC"), "")

    def test_case_7(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABAB", "ABABAB"), "AB")

class TestGcdOfStrings2(unittest.TestCase):
    def setUp(self):
        self.gcdOfStrings = Solution2()
    def test_case_1(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABCABC", "ABC"), "ABC")

    def test_case_2(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABABAB", "ABAB"), "AB")

    def test_case_3(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("LEET", "CODE"), "")

    def test_case_4(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("A", "A"), "A")

    def test_case_5(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("AAAA", "AA"), "AA")

    def test_case_6(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABCDEF", "ABC"), "")

    def test_case_7(self):
        self.assertEqual(self.gcdOfStrings.gcdOfStrings("ABAB", "ABABAB"), "AB")


# Measure execution time for unit tests
def run_tests():
    for test_class in [TestGcdOfStrings, TestGcdOfStrings2]:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        start_time = time.time()
        unittest.TextTestRunner().run(suite)
        end_time = time.time()
        print(f"{test_class.__name__} execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_tests()
