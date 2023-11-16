"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""
import re

class Solution(object):
    def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # row1 = set("qwertyuiop")
        # row2 = set("asdfghjkl")
        # row3 = set("zxcvbnm")

        # res = []
        # for word in words:
        #     w = set(word.lower())
        #     if w <= row1 or w <= row2 or w <= row3:
        #         res.append(word)
        
        # return res

    
        output = []
        for i in words:
            if(re.match('^[qwertyuiop]+$', i.lower()) or
             (re.match('^[asdfghjkl]+$', i.lower())) or
             (re.match('^[zxcvbnm]+$', i.lower()))):

             output.append(i)
        return output


print(Solution.findWords(["Hello","Alaska","Dad","Peace"]))