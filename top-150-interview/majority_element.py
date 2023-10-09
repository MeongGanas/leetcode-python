"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 
Example 1:

Input: nums = [3,2,3]
Output: 3
"""


class Solution(object):
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        return nums[n//2]


print(Solution.majorityElement([3, 2, 3]))
print(Solution.majorityElement([2, 2, 1, 1, 1, 2, 2, 3, 10, 10]))
