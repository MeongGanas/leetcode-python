"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""
class Solution(object):
    def commonChars(self, s):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        sett = set(s[0])
        r = []
        for one in sett:
            n = min([c.count(one) for c in s])
            if n >0:
                r += [one]*n
        return r 
        
solution = Solution()
print(solution.commonChars(["bella","label","roller"]))
print(solution.commonChars(["cool","lock","cook", "c"]))