"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""


class Solution(object):
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char = "abcdefghijklmnopqrstuvwxyz"
        for i in char:
            if s.count(i) != t.count(i):
                return False
        return True


print(Solution.isAnagram('anagram', 'nagaram'))
print(Solution.isAnagram('rat', 'cat'))
print(Solution.isAnagram('a', 'ab'))
