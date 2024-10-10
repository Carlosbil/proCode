"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

# SOLUTION

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # take the less length of the words
        len1 = len(word1)
        len2 = len(word2)
        min_len = min(len1, len2)
        sol = ""
        i = 0
        # while having enought length, add the letters in alternating order
        while i < min_len:
            sol = sol+word1[i]+word2[i]
            i += 1
        # add the remaining letters
        sol = sol + word1[min_len:] if len1 > len2 and len1 != len2   else sol + word2[min_len:]
        return sol
        
# Time complexity: O(n)
# Space complexity: O(n)

#Other Solutions:
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Use list to build the solution for better performance
        sol = []
        # Iterate over both words simultaneously using zip
        for char1, char2 in zip(word1, word2):
            sol.append(char1)
            sol.append(char2)
        # Add the remaining letters of the longer word
        sol.append(word1[len(word2):])
        sol.append(word2[len(word1):])
        # Join list to form the final string
        return ''.join(sol)
# Time complexity: O(n)
# Space complexity: O(n)