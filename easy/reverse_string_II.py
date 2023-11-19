"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
"""

class Solution(object):
    def reverseStr(s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        for i in range(0, len(s), 2*k):
            res += s[i:i+k][::-1]
            res += s[i+k:i+2*k]
        
        return res
        

        # index = 0 
        # length = len(s)
        # res=""
        # while index < length:
        #     if index + k > length:
               
        #         portion=s[index:length]
        #         res+=portion[::-1]
                
        #     else:
        #         portion=s[index:index+k]
        #         res+=portion[::-1]
        #         res+=s[index+k:index+2*k]
                
        #     index+=2*k
        # return res

print(Solution.reverseStr("abcdefg", 2))
print(Solution.reverseStr("abcdefghijk", 2))
print(Solution.reverseStr("abcd", 2))