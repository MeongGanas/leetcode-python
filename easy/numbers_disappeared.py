"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

class Solution(object):
    def findDisappearedNumbers(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        n_list = range(1, n + 1)
        answer = list(set(n_list) - set(nums))
        return answer

print(Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))