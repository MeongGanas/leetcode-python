"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # trusting = {}
        # trusted = {}
        # for i in range(1, n+1):
        #     trusting[i] = 0
        #     trusted[i] = 0

        # for people in trust:
        #     for i, p in enumerate(people):
        #         if i == 0:
        #             trusting[p] += 1
        #         else:
        #             trusted[p] += 1
        
        # for trust, t in zip(trusted.keys(), trusting.keys()):
        #     if trusted[trust] == (n - 1) and trusting[t] == 0:
        #         return trust

        # return -1

        trust_count = [0] * (n + 1)
    
        for a, b in trust:
            trust_count[a] -= 1  # a trusts someone, so decrement
            trust_count[b] += 1  # b is trusted, so increment
    
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:  # everyone trusts i except i itself
                return i
        
        return -1

solution = Solution()
print(solution.findJudge(2, [[1,2]]))
print(solution.findJudge(3, [[1,3],[2,3]]))
print(solution.findJudge(3, [[1,3],[2,3],[3,1]]))