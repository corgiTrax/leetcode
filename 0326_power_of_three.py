import sys

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 3: return True
        elif n % 3 != 0: return False
        else: return self.isPowerOfThree(n / 3)

sol = Solution()
print(sol.isPowerOfThree(int(sys.argv[1])))
        
