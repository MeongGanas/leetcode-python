"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
"""
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0


solution = Solution()
print(solution.isBoomerang([[1,1],[2,3],[3,2]]))
print(solution.isBoomerang([[1,1],[2,2],[3,3]]))
print(solution.isBoomerang([[5,4],[2,1],[3,2]]))