"""
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
 
"""
"""
If we concatenate the strigs and str1+str2 != str2+str1, then there is no common divisor.
if yes, then we can find the common divisor by checking the common letters between the two strings.

"""
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = math.gcd(len(str1), len(str2))
        
        return str1[:gcd_length]

"""
Other sol finded as the best in leetcode:
"""
class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Function to find the greatest common divisor of two strings
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        len1, len2 = len(str1), len(str2)
        # Find the GCD of the lengths
        gcd_length = gcd(len1, len2)
        
        # Potential GCD string
        gcd_string = str1[:gcd_length]
        
        # Check if both strings can be constructed by gcd_string
        if (gcd_string * (len1 // gcd_length) == str1) and (gcd_string * (len2 // gcd_length) == str2):
            return gcd_string
        else:
            return ""