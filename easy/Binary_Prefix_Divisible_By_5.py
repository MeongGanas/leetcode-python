"""
You are given a binary array nums (0-indexed).

We define xi as the number whose binary representation is the subarray nums[0..i] (from most-significant-bit to least-significant-bit).

For example, if nums = [1,0,1], then x0 = 1, x1 = 2, and x2 = 5.
Return an array of booleans answer where answer[i] is true if xi is divisible by 5.

 

Example 1:

Input: nums = [0,1,1]
Output: [true,false,false]
Explanation: The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
Example 2:

Input: nums = [1,1,1]
Output: [false,false,false]
"""
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        # res = []
        # temp = ''
        # for i in nums:
        #     temp += str(i)
        #     base_10 = int(temp, 2)
        #     res.append(base_10 % 5 == 0)
        # return res

        ans = []
        cur = 0
        for num in nums:
            cur = (cur * 2 + num) % 5
            ans.append(cur == 0)
        return ans

solution = Solution()
print(solution.prefixesDivBy5([0,1,1]))
print(solution.prefixesDivBy5([1,1,1]))