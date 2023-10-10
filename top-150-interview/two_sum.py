class Solution(object):
    def twoSum(nums, target):
        dict = {}
        for i, j in enumerate(nums):
            if (target - j) in dict:
                return [dict[target - j], i]
            dict[j] = i


print(Solution.twoSum([2, 7, 11, 15], 9))
print(Solution.twoSum([3, 2, 4], 6))
