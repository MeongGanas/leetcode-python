class Solution(object):
    def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """

        x = s.split()
        if len(x) > 1:
            for i in x:
                if i.isdigit():
                    return int(i)
        return int(s)


print(Solution.myAtoi(" -4193"))
