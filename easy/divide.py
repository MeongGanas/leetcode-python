class Solution(object):
    def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        res = int(dividend/divisor)
        if res > 0:
            return res
        return res - 1


print(Solution.divide(7, -3))
