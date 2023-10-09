"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

import re

class Solution(object):
    def isPalindrome(s):

        """
        :type s: str
        :rtype: bool
        """
        strng = ''.join(re.findall(r'[a-zA-Z0-9]+', s)).lower()
        return strng == strng[::-1]


print(Solution.isPalindrome("A man, a plan, a canal: Panama"))
print(Solution.isPalindrome("0P"))
