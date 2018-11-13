class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        return self.combination(m - 1 + n - 1, m - 1)

    def combination(self,n,k):
        return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))
