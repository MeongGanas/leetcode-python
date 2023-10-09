class Solution(object):
    def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            nums.append(target)
            nums.sort()

        i = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            i += 1


print(Solution.searchInsert([1, 3, 5, 6], 6))
