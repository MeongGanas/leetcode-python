"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        strng = ''

        for i in s:
            if i.isalpha():
                strng += i
        
        strng = strng[::-1]

        k = 0
        s = list(s)
        for j in range(len(s)):
            if s[j].isalpha():
                s[j] = strng[k]
                k += 1
        
        return ''.join(s)
        
solution = Solution()
print(solution.reverseOnlyLetters("ab-cd"))
print(solution.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
        