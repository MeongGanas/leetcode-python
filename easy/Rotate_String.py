"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
"""

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # if s == goal:
        #     return True
            
        # s_copy = list(s)
        # for i in range(len(s)-1):
        #     s_copy.pop(0)
        #     s_copy.append(s[i])

        #     if ''.join(s_copy) == goal:
        #         return True
            
        # return False

        return len(s) == len(goal) and s in goal+goal
        
solution = Solution()
print(solution.rotateString("abcde", "cdeab"))
print(solution.rotateString("abcde", "abced"))