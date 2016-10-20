import sys
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0: ele = "FizzBuzz"
            elif i % 5 == 0: ele = "Buzz"
            elif i % 3 == 0: ele = "Fizz"
            else: ele = str(i)
            result.append(ele)
 
class Solution1(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range(1, n + 1)]
        return [str(i)*(i%3!=0)*(i%5!=0) + 'Fizz'*(not i%3) + 'Buzz'*(not i%5) for i in xrange(1,n+1)]

sol = Solution1()
print(sol.fizzBuzz(int(sys.argv[1])))
