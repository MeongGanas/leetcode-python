"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


class Solution(object):
    def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # cara tidak efisien
        # if len(s) % 2 != 0:
        #     return False

        # pairs = ["{}", "()", "[]"]

        # for i in range(len(s)):
        #     for j in pairs:
        #         if j in s:
        #             s = ''.join(s.split(j))

        # return True if s == '' else False

        # cara paling efisien
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


print(Solution.isValid("()"))
print(Solution.isValid("()[]{}"))
print(Solution.isValid("(}"))
print(Solution.isValid("({})"))
print(Solution.isValid("({{}))"))
print(Solution.isValid("{[]}"))
print(Solution.isValid("(([]){})"))
print(Solution.isValid("([[][]{({}({}))}])"))
