"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""
class Solution(object):
    def process(self, l):
        result = []
        for i in l:
            if i != "#":
                result.append(i)
            elif result:
                result.pop()
        return result
    
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.process(s) == self.process(t)

solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))
print(solution.backspaceCompare("ab##", "a#c#"))