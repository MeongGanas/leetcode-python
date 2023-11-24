"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
"""

class Solution(object):
    def nextGreaterElement(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in nums1:
        #     index = nums2.index(i)
        #     for j in range(index+1, len(nums2)):
        #         if nums2[j] > nums2[index]:
        #             res.append(nums2[j])
        #             break
        #         elif j == len(nums2) - 1 and nums2[j] < nums2[index]:
        #             res.append(-1)
        #     if index+2 > len(nums2):
        #         res.append(-1)
        #     elif len(res) == 0:
        #         res.append(-1)
        # return res
        

        nums1_index = { n :i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                index = nums1_index[val]
                res[index] = cur
            if cur in nums1_index:
                stack.append(cur)
        
        return res

        

print(Solution.nextGreaterElement([4,1,2],[1,3,4,2]))
print(Solution.nextGreaterElement([2,4],[1,2,3,4]))
print(Solution.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))
        