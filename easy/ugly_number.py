"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""


class Solution(object):
    def isUgly(n):
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime

        return n == 1


print(Solution.isUgly(4))
print(Solution.isUgly(14))
print(Solution.isUgly(25))
print(Solution.isUgly(6))
print(Solution.isUgly(8))
