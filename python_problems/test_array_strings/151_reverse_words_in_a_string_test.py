import unittest
import time
from python_problems.array_strings.reverse_words_in_a_string import Solution, Solution2

class TestReverseWordsSolution(unittest.TestCase):
    def setUp(self):
        self.reverseWords = Solution()

    def test_case_1(self):
        self.assertEqual(self.reverseWords.reverseWords("the sky is blue"), "blue is sky the")

    def test_case_2(self):
        self.assertEqual(self.reverseWords.reverseWords("  hello world  "), "world hello")

    def test_case_3(self):
        self.assertEqual(self.reverseWords.reverseWords("a good   example"), "example good a")

    def test_case_4(self):
        self.assertEqual(self.reverseWords.reverseWords(" "), "")

    def test_case_5(self):
        self.assertEqual(self.reverseWords.reverseWords("single"), "single")

    def test_case_6(self):
        self.assertEqual(self.reverseWords.reverseWords("  multiple   spaces  "), "spaces multiple")

    def test_case_7(self):
        self.assertEqual(self.reverseWords.reverseWords("one two three"), "three two one")

    def test_case_8(self):
        self.assertEqual(self.reverseWords.reverseWords(" leading and trailing "), "trailing and leading")

    def test_case_9(self):
        self.assertEqual(self.reverseWords.reverseWords("repeat repeat repeat"), "repeat repeat repeat")

    def test_case_10(self):
        self.assertEqual(self.reverseWords.reverseWords(" a b  c "), "c b a")

# Unit tests para Solution2
class TestReverseWordsSolution2(unittest.TestCase):
    def setUp(self):
        self.reverseWords = Solution2()

    def test_case_1(self):
        self.assertEqual(self.reverseWords.reverseWords("the sky is blue"), "blue is sky the")

    def test_case_2(self):
        self.assertEqual(self.reverseWords.reverseWords("  hello world  "), "world hello")

    def test_case_3(self):
        self.assertEqual(self.reverseWords.reverseWords("a good   example"), "example good a")

    def test_case_4(self):
        self.assertEqual(self.reverseWords.reverseWords(" "), "")

    def test_case_5(self):
        self.assertEqual(self.reverseWords.reverseWords("single"), "single")

    def test_case_6(self):
        self.assertEqual(self.reverseWords.reverseWords("  multiple   spaces  "), "spaces multiple")

    def test_case_7(self):
        self.assertEqual(self.reverseWords.reverseWords("one two three"), "three two one")

    def test_case_8(self):
        self.assertEqual(self.reverseWords.reverseWords(" leading and trailing "), "trailing and leading")

    def test_case_9(self):
        self.assertEqual(self.reverseWords.reverseWords("repeat repeat repeat"), "repeat repeat repeat")

    def test_case_10(self):
        self.assertEqual(self.reverseWords.reverseWords(" a b  c "), "c b a")

def run_tests():
    for test_class in [TestReverseWordsSolution, TestReverseWordsSolution2]:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        start_time = time.time()
        unittest.TextTestRunner().run(suite)
        end_time = time.time()
        print(f"{test_class.__name__} execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    run_tests()