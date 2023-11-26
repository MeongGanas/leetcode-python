"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

Example 1:

Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
Example 2:

Input: left = 47, right = 85
Output: [48,55,66,77]
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # res = []

        # for i in range(left, right+1):
        #     num_str = str(i)
        #     temp = True
        #     for j in num_str:
        #         if int(j) != 0:
        #             if i % int(j) != 0:
        #                 temp = False
        #         else:
        #             temp = False
        #     if temp:
        #         res.append(i)

        # return res

        res=[]
        for i in range(left,right+1):
            a=i
            b=True
            while i:
                remainder=i%10
                if remainder==0 or a%remainder!=0:
                    b=False
                    break
                else:
                    i//=10
            if b:
                res+=[a]
        return res

print(Solution.selfDividingNumbers(1, 22))
print(Solution.selfDividingNumbers(47, 85))