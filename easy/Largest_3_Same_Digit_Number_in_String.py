class Solution(object):
    def largestGoodInteger(self, nums):
        """
        :type num: str
        :rtype: str
        """
        largest_number = '0'
        count = 1
        prev_number = int(nums[0])

        for i in range(1, len(nums)):
            current_number = nums[i]

            if int(current_number) == prev_number:
                count += 1
            else:
                count = 1

            if count == 3 and int(largest_number) <= int(current_number * 3):
                largest_number = current_number * 3
            
            prev_number = int(current_number)

        return largest_number if largest_number != '0' else ""
        

solution = Solution()
print(solution.largestGoodInteger("4818042931906802860005960222213336669500011846936171709111"))
print(solution.largestGoodInteger("42352338"))
print(solution.largestGoodInteger("2300019"))