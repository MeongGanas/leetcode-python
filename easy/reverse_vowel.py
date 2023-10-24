"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""


class Solution(object):
    def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        vowel = "aiueoAIUEO"

        vowel_in_s = []
        vowel_index = []
        for i in range(len(s)):
            if s[i] in vowel:
                vowel_in_s.append(s[i])
                vowel_index.append(i)

        vowel_in_s.reverse()

        for i in range(len(vowel_index)):
            s[vowel_index[i]] = vowel_in_s[i]

        return ''.join(s)


print(Solution.reverseVowels("hello"))
print(Solution.reverseVowels("leetcode"))
