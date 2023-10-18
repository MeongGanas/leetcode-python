class Solution(object):
    def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # order = [i for i in range(len(nums) + 1)]
        # res = list(set(order) - set(nums))
        # return res[0]

        n = len(nums)
        return (n * (n + 1)) / 2 - sum(nums)


print(Solution.missingNumber([0, 1]))
print(Solution.missingNumber([3, 0, 1]))
