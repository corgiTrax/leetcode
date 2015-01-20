#Solution 1
import math
class Solution1:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        possible_ways = 0
        if (n % 2 == 0):
            for i in range(n/2 + 1):
                possible_ways += self.combination_repetition(n - 2 * i + 1, i)
        else:
            for i in range(int(math.floor(n/2)) + 1):
                possible_ways += self.combination_repetition(n - 2 * i + 1, i)
        return possible_ways

    def combination(self,n,k):
        #returns n choose k
        return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))

    def combination_repetition(self,n,k):
        #returns combination with repitition 
        return self.combination(n + k - 1,k) 

#Solution 2: this is essentially fibonacci number
#think in terms of dynamic programming: the way to climb up to n stairs
#way(n) = way(n-1) + way(n-2)
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
sol = Solution()
print(sol.climbStairs(2))
