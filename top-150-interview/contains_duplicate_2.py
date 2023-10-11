"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution(object):
    def containsNearbyDuplicate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i - dict[v] <= k:
                return True
            dict[v] = i

        return False


print(Solution.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(Solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(Solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(Solution.containsNearbyDuplicate([99, 99], 2))
