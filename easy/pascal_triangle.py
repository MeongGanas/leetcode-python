"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 
"""


class Solution(object):
    def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if numRows == 1:
        #     return [[1]]

        # res = [[1], [1, 1]]
        # for i in range(2, numRows):
        #     prev = res[i-1]
        #     n = len(prev)
        #     temp = [1, 1]

        #     p = 1
        #     for j in range(1, n):
        #         temp.insert(p, prev[j] + prev[j-1])
        #         p += 1

        #     res.append(temp)
        # return res

        res = [[1]]
        for i in range(numRows-1):
            rowToAdd = [1]
            for j in range(i):
                rowToAdd.append(res[i][j] + res[i][j+1])
            rowToAdd.append(1)
            res.append(rowToAdd)
        return res


print(Solution.generate(1))
print(Solution.generate(2))
print(Solution.generate(3))
print(Solution.generate(4))
print(Solution.generate(5))
