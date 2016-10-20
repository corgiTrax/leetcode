import random
import sys
n = int(sys.argv[1])
a = random.randint(1,n)
print(a)

def guess(g):
    if a > g: return 1
    elif a < g: return -1
    else: return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1; high = n; 
        while 1:
            myGuess = (low + high) / 2
            res = guess(myGuess)
            if res == 0: return myGuess
            elif res == 1: low = myGuess + 1
            else: high = myGuess - 1

sol = Solution()
print(sol.guessNumber(n))
