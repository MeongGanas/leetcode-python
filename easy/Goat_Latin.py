"""
You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".
If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.
Return the final sentence representing the conversion from sentence to Goat Latin.

 

Example 1:

Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
"""

class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """ 
        # vowel = 'aiueo'

        # sentence = sentence.split()

        # res = []
        # for i, v in enumerate(sentence):
        #     if v[0].lower() in vowel:
        #         latin = v + 'ma' + ('a' * (i+1))
        #         res.append(latin)
        #     else:
        #         latin = v[1:] + v[0] + 'ma' + ('a' * (i+1))
        #         res.append(latin)

        # return ' '.join(res)

        ans = ""
        vowels = 'aAeEiIoOuU'
        
        for idx, word in enumerate(sentence.split()):
            if word[0] in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
                
            word += 'a' * (idx + 1)
            ans += word + ' '
                
        return ans[:-1]       


solution = Solution()
print(solution.toGoatLatin("I speak Goat Latin"))
print(solution.toGoatLatin("The quick brown fox jumped over the lazy dog"))