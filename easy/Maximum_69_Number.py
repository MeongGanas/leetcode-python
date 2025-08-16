class Solution:
    def maximum69Number (self, num: int) -> int:
        prevMax = 0
        numList = list(str(num))

        for i in range(len(numList)):
            changeToNine = numList.copy()
            changeToNine[i] = '9'
            changeToNine = int(''.join(changeToNine))

            changeToSix = numList.copy()
            changeToSix[i] = '6'
            changeToSix = int(''.join(changeToSix))

            if changeToNine > changeToSix:
                if changeToNine > prevMax:
                    prevMax = changeToNine
            else:
                if changeToSix > prevMax:
                    prevMax = changeToSix

        return prevMax
    
print(Solution().maximum69Number(9669))
print(Solution().maximum69Number(9996))
print(Solution().maximum69Number(9999))