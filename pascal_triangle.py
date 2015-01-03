import math
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            line = [self.combination(i,x) for x in range(i + 1)]
            triangle.append(line)

        return triangle

    def combination(self, n, k):
        '''returns n choose k'''
        return math.factorial(n)/(math.factorial(k) * math.factorial(n-k))

'''could also use recursion and dynamic programming, I suppose?'''


sol = Solution()
print(sol.generate(5))
