"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701

"""

class Solution(object):
    def titleToNumber(columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i in columnTitle:
            res = res * 26 + (ord(i) - ord('A') + 1) 

        return res
    
print(Solution.titleToNumber("A"))
print(Solution.titleToNumber("Z"))
print(Solution.titleToNumber("AA"))
print(Solution.titleToNumber("ZY"))