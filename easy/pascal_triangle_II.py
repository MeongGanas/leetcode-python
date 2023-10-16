"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""


class Solution(object):
    def getRow(rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        res = [[1]]
        for i in range(rowIndex):
            rowToAdd = [1]
            for j in range(i):
                rowToAdd.append(res[i][j] + res[i][j+1])
            rowToAdd.append(1)
            res.append(rowToAdd)
        return res[rowIndex]


print(Solution.getRow(1))
