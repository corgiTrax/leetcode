'''The question is essentially asking how many factors of 5 are there in n!
We can't just return n/5 because factors like 25 will have 2 factors of 5'''
import math
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        zero_count = 0
        div = 5
        while div <= n:
            zero_count += n//div
            div *= 5
        return zero_count 

sol = Solution()
print(sol.trailingZeroes(30))        
