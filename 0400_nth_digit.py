import sys
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0; d = 1
        while total < n:
            last_total = total
            total += 9 * (10 ** (d-1)) * d
            d += 1
        d -= 1
        start = 10 ** (d-1)
        which_num = start + (n - last_total - 1) / d
        print(d, total, last_total, start, which_num)
        return (str(which_num))[(n - last_total - 1) % d]

sol = Solution()
print(sol.findNthDigit(int(sys.argv[1])))
