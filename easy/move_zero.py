"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""


class Solution(object):
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # zero_count = nums.count(0)
        # while 0 in nums:
        #     nums.remove(0)
        # for i in range(zero_count):
        #     nums.append(0)
        # return nums

        n = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                if n != i:
                    nums[n], nums[i] = nums[i], 0
                n += 1


print(Solution.moveZeroes([0, 1, 0, 3, 12]))
print(Solution.moveZeroes([0, 0, 1]))
