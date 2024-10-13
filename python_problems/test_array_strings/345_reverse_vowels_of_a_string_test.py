import unittest
import time
from array_strings.reverse_vowels_of_a_string import Solution, Solution2

class TestReverseVowels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.reverseVowels("IceCreAm"), "AceCreIm")

    def test_example_2(self):
        self.assertEqual(self.solution.reverseVowels("leetcode"), "leotcede")

    def test_empty_string(self):
        self.assertEqual(self.solution.reverseVowels(""), "")

    def test_no_vowels(self):
        self.assertEqual(self.solution.reverseVowels("bcdfg"), "bcdfg")

    def test_all_vowels(self):
        self.assertEqual(self.solution.reverseVowels("aeiouAEIOU"), "UOIEAuoiea")

    def test_single_vowel(self):
        self.assertEqual(self.solution.reverseVowels("a"), "a")

    def test_mixed_case(self):
        self.assertEqual(self.solution.reverseVowels("AeiOu"), "uOieA")

    def test_vowels_at_beginning_and_end(self):
        self.assertEqual(self.solution.reverseVowels("abecedi"), "ibeceda")

    def test_vowels_with_numbers(self):
        self.assertEqual(self.solution.reverseVowels("l33tc0d3"), "l33tc0d3")

    def test_vowels_with_special_characters(self):
        self.assertEqual(self.solution.reverseVowels("!a!e!i!o!u!"), "!u!o!i!e!a!")
    
    def test_long_string(self):
        self.assertEqual(self.solution.reverseVowels("thisisaverylongstringwithvowels"), "thesosivirylongstrengwathviwils")

class TestReverseVowels2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test_example_1(self):
        self.assertEqual(self.solution.reverseVowels("IceCreAm"), "AceCreIm")

    def test_example_2(self):
        self.assertEqual(self.solution.reverseVowels("leetcode"), "leotcede")

    def test_empty_string(self):
        self.assertEqual(self.solution.reverseVowels(""), "")

    def test_no_vowels(self):
        self.assertEqual(self.solution.reverseVowels("bcdfg"), "bcdfg")

    def test_all_vowels(self):
        self.assertEqual(self.solution.reverseVowels("aeiouAEIOU"), "UOIEAuoiea")

    def test_single_vowel(self):
        self.assertEqual(self.solution.reverseVowels("a"), "a")

    def test_mixed_case(self):
        self.assertEqual(self.solution.reverseVowels("AeiOu"), "uOieA")

    def test_vowels_at_beginning_and_end(self):
        self.assertEqual(self.solution.reverseVowels("abecedi"), "ibeceda")

    def test_vowels_with_numbers(self):
        self.assertEqual(self.solution.reverseVowels("l33tc0d3"), "l33tc0d3")

    def test_vowels_with_special_characters(self):
        self.assertEqual(self.solution.reverseVowels("!a!e!i!o!u!"), "!u!o!i!e!a!")
    
    def test_long_string(self):
        self.assertEqual(self.solution.reverseVowels("thisisaverylongstringwithvowels"), "thesosivirylongstrengwathviwils")

def run_tests():
    for test_class in [TestReverseVowels, TestReverseVowels2]:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        start_time = time.time()
        unittest.TextTestRunner().run(suite)
        end_time = time.time()
        print(f"{test_class.__name__} execution time: {end_time - start_time:.4f} seconds")


if __name__ == '__main__':
    run_tests()
