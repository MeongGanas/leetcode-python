"""
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
"""
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        if x2 <= x3 or x4 <= x1:
            return False
        if y2 <= y3 or y4 <= y1:
            return False
        return True
        
solution = Solution()
print(solution.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
print(solution.isRectangleOverlap([0,0,1,1], [1,0,2,1]))
print(solution.isRectangleOverlap([0,0,1,1], [2,2,3,3]))
print(solution.isRectangleOverlap([8,20,12,20], [14,2,19,11]))
print(solution.isRectangleOverlap([2,17,6,20], [3,8,6,20]))
print(solution.isRectangleOverlap([5,15,8,18], [0,3,7,9]))
print(solution.isRectangleOverlap([7,8,13,15], [10,8,12,20]))