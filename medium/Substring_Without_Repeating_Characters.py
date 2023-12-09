"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right_pointer = 0

        seen = ''
        max_length = 0

        while right_pointer < len(s):
            if s[right_pointer] not in seen:
                seen += s[right_pointer]
            else:
                length = len(seen)
                if length > max_length:
                    max_length = length
                
                idx = seen.index(s[right_pointer])
                seen = seen[idx+1:] + s[right_pointer]
            right_pointer += 1

        max_length = max(max_length, len(seen))
        
        return max_length
        

solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))
# print(solution.lengthOfLongestSubstring("dvdf"))
# print(solution.lengthOfLongestSubstring(" "))
# print(solution.lengthOfLongestSubstring("pwwkew"))
print(solution.lengthOfLongestSubstring("aabaab!bb"))