"""
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

"""
from heapq import *

class Solution(object):
    def findRelativeRanks(score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # sort = sorted(score)

        # rank = []
        # for i in range(len(sort)-1, -1, -1):
        #     rank.append(score.index(sort[i]))

        # for j in range(len(score)):
        #     for k in rank:
        #         if j == k and rank.index(k) == 0:
        #             score[j] = "Gold Medal"
        #         elif j == k and rank.index(k) == 1:
        #             score[j] = "Silver Medal"
        #         elif j == k and rank.index(k) == 2:
        #             score[j] = "Bronze Medal"
        #         elif j == k and rank.index(k) > 2:
        #             score[j] = str(rank.index(k) + 1)
            
        # return score
    

        heap, res, count = [], [0] * len(score), 0
        for i in range(len(score)):heappush(heap, (-score[i],i))
        while heap:
            idx  = heappop(heap)[1]
            if count == 0:res[idx] = "Gold Medal"
            elif count == 1:res[idx] = "Silver Medal"
            elif count == 2:res[idx] = "Bronze Medal"
            else:res[idx] = str(count + 1)
            count += 1
        return res

        
print(Solution.findRelativeRanks([5, 4, 3, 2, 1]))
print(Solution.findRelativeRanks([10,3,8,9,4]))