"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
"""
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        top_index = arr.index(max(arr))
        n = len(arr)

        if top_index == 0 or top_index == n-1:
            return False
        
        left = arr[:top_index]
        right = arr[top_index:]

        for i in range(len(left)-1):
            if left[i+1] <= left[i]:
                return False
        for j in range(len(right)-1):
            if right[j+1] >= right[j]:
                return False

        return True
        
solution = Solution()
print(solution.validMountainArray([2,1]))
print(solution.validMountainArray([3,5,5]))
print(solution.validMountainArray([0,3,2,1]))
print(solution.validMountainArray([0,2,2,3,5,2,1]))
print(solution.validMountainArray([0,1,2,3,4,5,6,7,8,9]))
print(solution.validMountainArray([3,6,5,6,7,6,5,3,0]))