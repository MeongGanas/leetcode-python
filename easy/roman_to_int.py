class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # res = 0
        # s = list(s)
        # for i in range(len(s)):
        #     if s[i] == "I" or s[i] == "X" or s[i] == "C":
        #         try:
        #             if s[i+1] != "I" and s[i+1] != "X" and s[i+1] != "C":
        #                 res += (roman[s[i+1]] - roman[s[i]])
        #         except:
        #             res += (roman[s[i]] - roman[s[i-1]])
        # return res


print(Solution.romanToInt("XV"))
