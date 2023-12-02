"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
Example 2:

Input: nums = [2,3]
Output: [2,3]
"""

class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # odd = []
        # even = []

        # for i in nums:
        #     if i % 2 == 0:
        #         even.append(i)
        #     else:
        #         odd.append(i)

        # res = []
        # for i, v in zip(odd, even):
        #     res.append(i)
        #     res.append(v)

        # return res

        odd=1
        evn=0
        new=[0]*len(nums)
        for num in nums:
            if num%2==0:
                new[evn]=num
                evn+=2
            else:
                new[odd]=num
                odd+=2
        return new



solution = Solution()
print(solution.sortArrayByParityII([4,2,5,7]))
