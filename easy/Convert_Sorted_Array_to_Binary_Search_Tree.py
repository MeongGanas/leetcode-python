# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"ListNode{{val: {self.val}, left: {repr(self.left)}, right: {repr(self.right)}}}"

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
         
        mid = len(nums)//2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
print(Solution().sortedArrayToBST([1,3]))

