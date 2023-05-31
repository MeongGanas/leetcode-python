class Solution(object):
    def twoSum(nums, target):
        # count = 1
        # for i in range(0, len(nums)):
        #     for j in range(count, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
        #     count += 1

        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        return []


print(Solution.twoSum([2, 7, 11, 15], 9))
