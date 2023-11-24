"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0

"""

class Solution(object):
    def findLHS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else :
                dic[i]=1
        ans = [0] 
        for i in dic:
            if i+1 in dic:
                ans.append(dic[i]+dic[i+1])
        
        return max(ans)


print(Solution.findLHS([1,2,3,4]))
print(Solution.findLHS([1,1,1,1]))
print(Solution.findLHS([1,3,2,2,5,2,3,7]))