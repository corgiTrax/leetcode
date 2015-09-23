class Solution(object):
    '''recursion version'''
    def addDigits(self, num):
        if num < 10: return num
        else: return self.addDigits(self.sumDigits(num))

    def sumDigits(self,num):
        '''sum all digits, recursion'''
        if num < 10: return num
        else: return num % 10 + self.sumDigits(num / 10)

class Solution(object):
    '''O(1) time version'''
    def addDigits(self, num):
        answer = num % 9
        if answer == 0 and num != 0: answer = 9
        return answer 


import sys
num = int(sys.argv[1])
sol = Solution()
print(sol.addDigits(num))
