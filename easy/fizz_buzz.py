class Solution(object):
    def fizzBuzz(n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 
                else 'Fizz' if i % 3 == 0 
                else 'Buzz' if i % 5 == 0 
                else str(i) 
                for i in range(1, n+1)]
        

print(Solution.fizzBuzz(3))
print(Solution.fizzBuzz(5))
print(Solution.fizzBuzz(15))