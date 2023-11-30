"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
"""
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        # uniq = {}
        # for i in re.split(r'\W+', paragraph):
        #     i = re.sub('[^A-Za-z0-9]+', '', i).lower()
        #     if i not in banned:
        #         if i not in uniq:
        #             uniq[i] = 1
        #         else:
        #             uniq[i] += 1
        
        # res = ""
        # temp = 0
        # for j in uniq:
        #     if uniq[j] > temp:
        #         res = j
        #         temp = uniq[j]
        
        # return res

        lst = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        lst_set = set(lst) - set(banned)
        
        max_cnt = 0
        max_word = ''

        for word in lst_set:
            if max_cnt <= lst.count(word):
                max_cnt = lst.count(word)
                max_word = word
        
        return max_word
        

solution = Solution()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
print(solution.mostCommonWord("a, a, a, a, b,b,b,c, c", ['a']))
print(solution.mostCommonWord("Bob!", ['hit']))
                