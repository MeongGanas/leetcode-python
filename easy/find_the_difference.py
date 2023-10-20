class Solution(object):
    def findTheDifference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in t:
            if t.count(i) != s.count(i):
                return i


print(Solution.findTheDifference("abcd", "abcde"))
print(Solution.findTheDifference("a", "aa"))
