import sys

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # note that the ^ operator takes integer in decimal, not binary! it will convert decimal into binary
        return bin(x^y).count("1")

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(int(sys.argv[1]), int(sys.argv[2])))
