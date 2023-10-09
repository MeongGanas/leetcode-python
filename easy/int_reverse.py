class Solution(object):
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        if len(y) > 9:
            return 0
        elif x >= 0:
            return int(y[::-1])
        return int('-{val}'.format(val=y[1:][::-1]))


print(Solution.reverse(1534236469))
