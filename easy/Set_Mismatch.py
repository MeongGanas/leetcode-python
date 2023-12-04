"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s, n = set(nums), len(nums)
        for i in range(1, n+1):
            if i not in s:
                t = i
                break
        
        s1 = sum(nums)
        s2 = (n*(n+1))//2
        d = s2 - s1

        return t-d, t

solution = Solution()
print(solution.findErrorNums([1, 2, 2, 4]))
print(solution.findErrorNums([2, 2]))
print(solution.findErrorNums([1, 1]))