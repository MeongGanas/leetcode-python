"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
"""

class Solution(object):
    def hammingDistance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = "{0:b}".format(x ^ y).count("1")
        
        return ans

print(Solution.hammingDistance(1, 4))
print(Solution.hammingDistance(3, 1))
print(Solution.hammingDistance(93, 73))
print(Solution.hammingDistance(4, 2))
        