"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
"""
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # uncommon = []
        # s1 = s1.split()
        # s2 = s2.split()

        # for i in s1:
        #     if i not in s2 and s1.count(i) == 1:
        #         uncommon.append(i)

        # for j in s2:
        #     if j not in s1 and s2.count(j) == 1:
        #         uncommon.append(j)

        # return uncommon

        uncommonWords=[]
        s=s1.split()+s2.split()
        for i in s:
            if s.count(i)==1:uncommonWords.append(i) 
        return uncommonWords
        
        
solution = Solution()
print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))