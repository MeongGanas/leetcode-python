"""
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

 

Example 1:

Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1]. 
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.
Example 2:

Input: area = 37
Output: [37,1]
Example 3:

Input: area = 122122
Output: [427,286]
"""
from math import sqrt

class Solution(object):
    def constructRectangle(area):
        """
        :type area: int
        :rtype: List[int]
        """
        # root = int(math.sqrt(area))

        # left = area // root

        # while (left * root) != area:
        #     root += 1
        #     left = area // root

        # if root >= left:
        #     return [root, left]
        
        # return [left, root]

        for x in range(int(sqrt(area)), 0, -1):
            if area % x == 0:
                return[area//x, x]
        

print(Solution.constructRectangle(4))
print(Solution.constructRectangle(37))
print(Solution.constructRectangle(122122))