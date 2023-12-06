"""
You are given an integer array deck where deck[i] represents the number written on the ith card.

Partition the cards into one or more groups such that:

Each group has exactly x cards where x > 1, and
All the cards in one group have the same integer written on them.
Return true if such partition is possible, or false otherwise. 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
"""
class Solution(object):
    def gdc(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.gdc(b, a % b)
        
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) <= 1:
            return False
        
        uniq = dict()
        for i in deck:
            if i not in uniq:
                uniq[i] = 1
            else:
                uniq[i] += 1

        g = uniq[deck[0]]

        for v in uniq.values():
            g = self.gdc(g, v)
            print(g)
            if g == 1:
                return False

        return True
        

solution = Solution()
print(solution.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(solution.hasGroupsSizeX([1,1,1,2,2,2,3,3]))
# print(solution.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))