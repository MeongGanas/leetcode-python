"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution(object):
    def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final, count = 0, 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count > final:
                    final = count
                count = 0

        if count > final:
            final = count

        return final

    
print(Solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(Solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))