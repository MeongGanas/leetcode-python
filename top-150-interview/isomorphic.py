"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
"""


class Solution(object):
    def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # cara 1
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]

        change_s = ''.join([s_to_t[j] for j in s])
        change_t = ''.join([t_to_s[k] for k in t])

        return change_s == t and change_t == s

        # cara tercepat
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


print(Solution.isIsomorphic("egg", "add"))
print(Solution.isIsomorphic("foo", "bar"))
print(Solution.isIsomorphic("paper", "title"))
print(Solution.isIsomorphic("badc", "baba"))
