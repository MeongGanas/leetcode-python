"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution(object):
    def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]

        for word in strs:
            i = 0
            while i < len(word) and i < len(prefix) and prefix[i] == word[i]:
                i += 1
            prefix = prefix[:i]

        return prefix


print(Solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution.longestCommonPrefix(["a"]))
print(Solution.longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution.longestCommonPrefix(["car", "cir"]))
