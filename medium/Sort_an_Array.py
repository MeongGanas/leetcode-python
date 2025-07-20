import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        
        pivot = random.choice(nums)
        left = []
        eq = []
        right = []

        for num in nums:
            if pivot < num:
                right.append(num)
            elif pivot == num:
                eq.append(num)
            else:
                left.append(num)
            
        return self.sortArray(left) + eq + self.sortArray(right)

cases = [
    [5,2,3,1],
    [5,1,1,2,0,0],
    [2, 3, 1]
]

for case in cases:
    print(Solution().sortArray(case))