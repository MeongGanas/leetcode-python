class Solution(object):
    def titleToNumber(columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        for i in columnTitle:
            res = res * 26 + (ord(i) - ord('A') + 1) 

        return res
    
print(Solution.titleToNumber("A"))
print(Solution.titleToNumber("Z"))
print(Solution.titleToNumber("AA"))
print(Solution.titleToNumber("ZY"))