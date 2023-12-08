"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
"""
class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total = sum(arr)
        if total % 3 != 0: return False
        
        res, count, equal = 0, 0, total // 3
        for i in arr:
            count += i
            if count == equal:
                res += 1
                count = 0

        return res >= 3

solution = Solution()
print(solution.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(solution.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(solution.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
print(solution.canThreePartsEqualSum([1,-1,1,-1]))
print(solution.canThreePartsEqualSum([0,0,0,0]))
print(solution.canThreePartsEqualSum([10,-10,10,-10,10,-10,10,-10]))