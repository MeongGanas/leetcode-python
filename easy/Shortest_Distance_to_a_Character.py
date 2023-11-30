"""
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

 

Example 1:

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
Example 2:

Input: s = "aaab", c = "b"
Output: [3,2,1,0]
"""

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        # c_index = [i for i, v in enumerate(s) if v == c]

        # if len(c_index) == 1:
        #     res = [abs(c_index[0] - i) for i in range(len(s))]
        #     return res

        # res = []
        
        # prev = 0
        # next = 1

        # for i in range(len(s)):
        #     if c_index[next] == i and next < len(c_index)-1:
        #         prev = next
        #         next += 1
        #     calc = min(abs(i - c_index[prev]), abs(i - c_index[next]))
        #     res.append(calc)

        # return res

        n = len(s)
        right = [None]*n
        left = [None]*n
        answer = [None]*n

        temp = float("inf")
        for i in range(n):
            if s[i] == c:
                temp = 0
            left[i] = temp
            temp += 1

        temp = float("inf")
        for i in range(n-1,-1,-1):
            if s[i] == c:
                temp = 0
            right[i] = temp
            temp += 1   
            
        for i in range(n):
            answer[i] = min(right[i],left[i])

        return answer

solution = Solution()
print(solution.shortestToChar("loveleetcode", "e"))
print(solution.shortestToChar("aaab", "b"))