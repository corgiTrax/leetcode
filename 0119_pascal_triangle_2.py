import sys
import math
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return [self.comb(rowIndex - 1, r) for r in range(rowIndex)]

    def comb(self, n,r):
        return math.factorial(n)/(math.factorial(r) * math.factorial(n - r))

sol = Solution()
print(sol.getRow(int(sys.argv[1])))
