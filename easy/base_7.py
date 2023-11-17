"""
Given an integer num, return a string of its base 7 representation.

 

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
"""

class Solution(object):
    def convertToBase7(num):
        """
        :type num: int
        :rtype: str
        """

        res = ""
        real = abs(num)
        while real != 0:
            res = str(real % 7) + res
            real //= 7

        if num < 0:
            return "-" + res
        elif num == 0:
            return "0"
        return res
        

print(Solution.convertToBase7(100))
print(Solution.convertToBase7(-7))