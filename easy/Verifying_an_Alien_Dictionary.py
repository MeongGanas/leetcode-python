"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alp = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(26):
            d[order[i]] = alp[i]

        def f(word):
            normal = ''
            for i in word:
                normal += d[i]
            return normal

        for i in range(len(words)-1):
            if f(words[i]) > f(words[i+1]):
                return False

        return True


solution = Solution()
print(solution.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(solution.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(solution.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
print(solution.isAlienSorted(["kuvp","q"],"ngxlkthsjuoqcpavbfdermiywz"))