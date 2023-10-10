"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution(object):
    def wordPattern(pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        char_to_word = {}
        word_to_char = {}
        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False

            if word in word_to_char and word_to_char[word] != char:
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True


print(Solution.wordPattern('abba', 'dog cat cat dog'))
print(Solution.wordPattern('abba', 'dog dog dog dog'))
print(Solution.wordPattern('aba', 'dog cat cat dog'))
print(Solution.wordPattern('abab', 'dog cat cat fish'))
print(Solution.wordPattern('aba', 'dog cat cat'))
print(Solution.wordPattern('a', 'a'))
print(Solution.wordPattern('abc', 'b c a'))
