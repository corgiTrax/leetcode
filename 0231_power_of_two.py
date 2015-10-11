# brute force recursive solution
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 2: return True
        elif n % 2 != 0: return False
        else: return self.isPowerOfTwo(n / 2)

# using bitwise and
# also using the fact that in binary, 2^x is of form 100..., 2^x - 1 is of form 111...
class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1)) == 0
        
sol = Solution()
print(sol.isPowerOfTwo(24))
