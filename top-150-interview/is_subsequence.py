"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""


class Solution(object):
    def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        remainder_of_t = iter(t)

        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True


print(Solution.isSubsequence("abc", "ahbgdc"))
print(Solution.isSubsequence("axc", "ahbgdc"))
print(Solution.isSubsequence("acb", "ahbgdc"))
print(Solution.isSubsequence("aaaaaa", "bbaaaa"))
