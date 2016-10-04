class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
 
 class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ct = 0
        while n > 0:
            ct += n % 2
            n /= 2
        return ct
       
