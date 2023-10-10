class Solution(object):
    def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        # Cara 1
        prev = []
        while n != 1:
            n = sum(map(lambda x: x**2, map(int, str(n))))

            if n in prev:
                return False
            prev.append(n)

        return True

        # Cara 2
        # while (len(str(n)) > 1):
        #     temp = 0
        #     for x in str(n):
        #         temp += int(x) ** 2
        #     n = temp

        # if n != 1 and n != 7:
        #     return False
        # else:
        #     return True


print(Solution.isHappy(19))
print(Solution.isHappy(2))
print(Solution.isHappy(7))
