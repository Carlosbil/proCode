/*
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

If we concatenate the strigs and str1+str2 != str2+str1, then there is no common divisor.
if yes, then we can find the common divisor by checking the common letters between the two strings.

*/

package array_strings

// GcdOfStrings devuelve el máximo divisor común de dos cadenas
func GcdOfStrings(str1 string, str2 string) string {
	// Si la concatenación de str1 y str2 es distinta que la de str2 y str1, no tienen GCD
	if str1+str2 != str2+str1 {
		return ""
	}

	// Calculamos el GCD de las longitudes de las dos cadenas
	gcdLength := gcd(len(str1), len(str2))

	// Devolvemos el prefijo común que tiene longitud igual al GCD de las longitudes
	return str1[:gcdLength]
}

// gcd calcula el máximo común divisor de dos números
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
