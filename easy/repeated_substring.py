"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""

class Solution(object):
    def repeatedSubstringPattern(s):
        """
        :type s: str
        :rtype: bool
        """
        # i = len(s) - 1
        # while i != 0:
        #     for j in range(0, len(s), i):
        #         substring = s[j:j+i]
        #         if substring * (len(s) // len(substring)) == s:
        #             return True
        #     i -= 1

        # return False
        
        res=(s+s)[1:-1]
        return s in res


print(Solution.repeatedSubstringPattern("abab"))
print(Solution.repeatedSubstringPattern("aba"))
print(Solution.repeatedSubstringPattern("abaababaab"))
print(Solution.repeatedSubstringPattern("abac"))
print(Solution.repeatedSubstringPattern("ababab"))