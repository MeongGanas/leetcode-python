"""
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
"""

class Solution(object):
    def matrixReshape(mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # item = [j for i in mat for j in i]

        # if r * c != len(item):
        #     return mat

        # res = []
        
        # index_item = 0
        # for i in range(r):
        #     res.append(item[index_item:index_item+c])
        #     index_item = index_item + c
    
        # return res

        flat = []
        for i in mat:
            flat += i

        if r * c != len(flat):
            return mat

        res = []
        
        for i in range(0, len(flat), c):
            res.append(flat[i:i+c])
            
        return res
        
print(Solution.matrixReshape([[1,2],[3,4]], 1, 4))
print(Solution.matrixReshape([[1,2],[3,4]], 2, 4))
print(Solution.matrixReshape([[1,2,3,4]], 2, 2))