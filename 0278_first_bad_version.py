# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
import random
import sys
n = int(sys.argv[1]) # number of version
k = random.randint(1,n)
def isBadVersion(version):
    if version < k: return False
    else: return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
#        for i in range(1, n + 1):
#            if isBadVersion(i) == True: return i
        begin = 1; end = n; 
        while True:
            mid = (begin + end) / 2
            bad = isBadVersion(mid)
            if bad and (mid == 1 or not isBadVersion(mid - 1)): return mid
            elif bad: end = mid - 1
            else: begin = mid + 1
                
sol = Solution()
print(k)
print(sol.firstBadVersion(n))


