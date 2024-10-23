import unittest
from python_problems.array_strings.product_of_array_except_self import Solution


class TestProductExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_case_1(self):
        # Caso de ejemplo enunciado
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_case_2(self):
        # Caso con ceros
        self.assertEqual(self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
    
    def test_single_element(self):
        # Caso de un solo elemento
        self.assertEqual(self.solution.productExceptSelf([5]), [1])

    def test_two_elements(self):
        # Caso con dos elementos
        self.assertEqual(self.solution.productExceptSelf([2, 3]), [3, 2])

    def test_all_zeros(self):
        # Caso con todos los elementos siendo cero
        self.assertEqual(self.solution.productExceptSelf([0, 0, 0]), [0, 0, 0])

    def test_all_ones(self):
        # Caso con todos los elementos siendo uno
        self.assertEqual(self.solution.productExceptSelf([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_negative_numbers(self):
        # Caso con todos los elementos siendo negativos
        self.assertEqual(self.solution.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6])

    def test_mixed_positive_and_negative(self):
        # Caso con elementos positivos y negativos
        self.assertEqual(self.solution.productExceptSelf([1, -1, 2, -2, 3]), [12, -12, 6, -6, 4])

    def test_large_numbers(self):
        # Caso con números grandes
        self.assertEqual(self.solution.productExceptSelf([1000, 2000, 3000, 4000]), [24000000000, 12000000000, 8000000000, 6000000000])

    def test_repeated_elements(self):
        # Caso con elementos repetidos
        self.assertEqual(self.solution.productExceptSelf([2, 2, 2, 2]), [8, 8, 8, 8])

if __name__ == '__main__':
    unittest.main()
