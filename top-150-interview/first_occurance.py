"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""
class Solution(object):
    def strStr(haystack, needle):


        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


print(Solution.strStr("sadbutsad", "sad"))
print(Solution.strStr("leetcode", "leeta"))
print(Solution.strStr("hello", "ll"))
print(Solution.strStr("mississippi", "issi"))
