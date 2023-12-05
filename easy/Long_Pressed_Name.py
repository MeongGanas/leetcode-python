"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        j = 0
        i = 0
        n = len(name)
        t = len(typed)
        
        while j < t:
            if i < n and name[i] == typed[j]:
                i +=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            j +=1
        return i == n


solution = Solution()
print(solution.isLongPressedName("alex", "aaleex"))
print(solution.isLongPressedName("alex", "aaleexa"))
print(solution.isLongPressedName("saeed", "ssaaedd"))
print(solution.isLongPressedName("leelee", "lleeelee"))