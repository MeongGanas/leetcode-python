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
        hex_ = []
        negative = 0
        if num < 0: 
            num = 2**31 + num
            negative = 8
        while num/16.0 >= 1:
            hex_.append(num%16)
            num = num //16
        hex_.append(num+negative)
        hex_ = hex_[::-1]
        while negative == 8 and len(hex_) != 8:
            hex_.append(0)
        rep = "0123456789abcdef"
        for i in range(len(hex_)):
            hex_[i] = rep[hex_[i]]
        return ''.join(hex_)



print(Solution.toHex(26))
print(Solution.toHex(0))
print(Solution.toHex(-1))
print(Solution.toHex(-2))
print(Solution.toHex(-10))