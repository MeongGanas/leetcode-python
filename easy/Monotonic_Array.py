"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
"""
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        prev = nums[0]
        max_num = max(nums)

        if prev < max_num:
            for i in range(1, len(nums)):
                if nums[i] < prev:
                    return False
                prev = nums[i]
        else:
            for i in range(1, len(nums)):
                if nums[i] > prev:
                    return False
                prev = nums[i]
        return True

solution = Solution()
print(solution.isMonotonic([1,2,2,3]))
print(solution.isMonotonic([6,5,5,4]))
print(solution.isMonotonic([1,3,2]))