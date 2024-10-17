"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        reverse=[]
        for letter in s:
            if letter in vowels:
                reverse = [letter] + reverse
        
        for x in range(len(s)):
            if s[x] in vowels:
                s = s[:x] + reverse[0] + s[x+1:]
                reverse.pop(0)
        return s

# FASTEST SOLUTION
class Solution2:
    def reverseVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        s_list=list(s)
        l=0
        r=len(s_list)-1
        while r>l:
            if s_list[l] not in vowels:
                l+=1
            elif s_list[r] not in vowels:
                r-=1
            else:
                s_list[l],s_list[r]=s_list[r],s_list[l]
                l+=1
                r-=1
        return ''.join(s_list)

