"""
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
"""

class Solution(object):
    def toHex(num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num += 2**32
        hex_number = ""
        hex_digits = "0123456789abcdef"
        while(num>0):
            remender = num % 16
            hex_number = hex_digits[remender] + hex_number
            num /= 16
        if hex_number != "":
            return(hex_number)
        else:
            return "0"



print(Solution.toHex(26))
print(Solution.toHex(0))
print(Solution.toHex(-1))
print(Solution.toHex(-2))
print(Solution.toHex(-10))