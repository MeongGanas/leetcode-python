# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        length = len(nums)
        left = nums[0:length//2]
        mid = nums[length//2]
        right = nums[length//2+1:]

        return left, mid, right

print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
print(Solution().sortedArrayToBST([1,3]))