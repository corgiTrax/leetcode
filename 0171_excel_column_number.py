class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        number = 0
        for i in range(len(s)):
            #s[0] is actually the highest digit
            number += (ord(s[i]) - ord('A') + 1) * (26**(len(s) - i - 1))
        return number

sol = Solution()
print(sol.titleToNumber('AB'))
