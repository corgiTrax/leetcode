class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dict_num = {} # record the number that appears
        while (True):
            digits = [int(i) for i in str(n)]
            n = 0
            for digit in digits: n += digit**2
            if n == 1: return True
            elif str(n) in dict_num: return False
            else: dict_num[str(n)] = 1 
sol = Solution()
print(sol.isHappy(2))
