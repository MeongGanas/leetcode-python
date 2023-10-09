"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution(object):
    def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # s = s.split(" ")
        # pattern = list(pattern)
        # return len(set(s)) == len(set(pattern)) and len(pattern) == len(s)


print(Solution.wordPattern('abba', 'dog cat cat dog'))
print(Solution.wordPattern('aba', 'dog cat cat dog'))
print(Solution.wordPattern('aba', 'dog cat cat'))
