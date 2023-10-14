"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""


class Solution(object):
    def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        # Initialize search range for the square root
        start = 1
        end = x
        mid = -1

        # Perform binary search
        while (start <= end):
            print(mid, start, end)
            mid = start + (end - start) / 2

            # if square of the mid is > x, move the end to the left
            if mid*mid > x:
                end = mid - 1

            # if square of the mid is = x, we found it, return mid
            elif mid*mid == x:
                return mid

            # if square of the mid is < x, move the start to the right
            else:
                start = mid + 1

        # loop ends when start is > end, end is the integer value of the square root
        return end


print(Solution.mySqrt(4))
print(Solution.mySqrt(8))
