"""
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

 

Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
"""

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        # count = 0
        # letter = s[0]
        # i_start = 0
        # i_end = 0

        # res = []

        # for i, v in enumerate(s):
        #     if v == letter:
        #         count += 1
        #         i_end = i
        #     else:
        #         if count >= 3:
        #             res.append([i_start, i_end])
        #         letter = v
        #         i_start = i
        #         count = 1

        # if count >= 3:
        #     res.append([i_start, i_end])

        # return res
        

        res= []
        i=0
        j=1
        while j<len(s) and j <len(s):
            if s[i]==s[j]:
                j+=1
            else:
                if j-i >=3:
                    res.append([i,j-1])
                i=j
                j+=1 
            if j==len(s):
                if j-i>=3:
                    res.append([i,j-1])     
        return res  

solution = Solution()
print(solution.largeGroupPositions("abbxxxxzzy"))
print(solution.largeGroupPositions("abc"))
print(solution.largeGroupPositions("abcdddeeeeaabbbcd"))