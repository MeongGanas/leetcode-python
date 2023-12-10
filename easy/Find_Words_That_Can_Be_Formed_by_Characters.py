"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
class Solution(object):
    # def countCharacters(self, words, chars):
    #     """
    #     :type words: List[str]
    #     :type chars: str
    #     :rtype: int
    #     """
    #     res = 0
    #     for word in words:
    #         temp = 0
    #         for chr in set(word):
    #             c = word.count(chr)
    #             if c <= chars.count(chr):
    #                 temp += c
    #         if temp == len(word):
    #             res += len(word)

    #     return res
    
    def countCharacters(self, words, chars):
        counts = [0] * 26

        # Step 1: Initialize Character Counts Array
        for ch in chars:
            counts[ord(ch) - ord('a')] += 1

        result = 0

        # Step 3: Check Words
        for word in words:
            if self.canForm(word, counts):
                # Step 4: Calculate Lengths
                result += len(word)

        return result

    def canForm(self, word, counts):
        c = [0] * 26

        # Step 2: Update Counts Array
        for ch in word:
            x = ord(ch) - ord('a')
            c[x] += 1
            if c[x] > counts[x]:
                return False

        return True
    
solution = Solution()
print(solution.countCharacters(["cat","bt","hat","tree"], "atach"))
print(solution.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))