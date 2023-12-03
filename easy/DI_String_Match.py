"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

 

Example 1:

Input: s = "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: s = "III"
Output: [0,1,2,3]
Example 3:

Input: s = "DDI"
Output: [3,2,0,1]
"""
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        start = 0
        end = len(s)
        perm = [i for i in range(start, end + 1)]

        res = []

        for i in s:
            if i == 'I':
                res.append(perm[start])
                start += 1
            else:
                res.append(perm[end])
                end -= 1
        res.append(perm[start])
        
        return res

solution = Solution()
print(solution.diStringMatch("IDID"))
print(solution.diStringMatch("DDDI"))