"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""
class Solution(object):
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: int
        """
        # S = set(s)

        # if len(S) == 1:
        #     return len(s)
        
        # uniq = {}
        # for i in S:
        #     if i not in uniq:
        #         uniq[i] = s.count(i)
        #     else:
        #         uniq[i] += 1

        # res = 1
        # for j in uniq:
        #     res += uniq[j] - (uniq[j] % 2)
        # return res if res <= len(s) else res - 1


        # cara paling efisien
        ans = 0
        pair = set()
        for char in s:
            if char in pair:
                ans += 2
                pair.remove(char)
            else:
                pair.add(char)
        if pair:
            ans += 1
        return ans


print(Solution.longestPalindrome('abccccdd'))
print(Solution.longestPalindrome('a'))
print(Solution.longestPalindrome('ccc'))
print(Solution.longestPalindrome('abb'))
print(Solution.longestPalindrome('tattarrattat'))
        