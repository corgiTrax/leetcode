import sys
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        note: without extra space
        """
        if x < 0 or (x != 0 and x % 10 == 0): return False
        # to get number of digits
        # can do len(str(x)), but requires additional space
        # can do int(math.log10(x)) + 1 if allow to use math lib
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x /= 10
        return rev == x or x == rev / 10

class Solution1(object):
    def isPalindrome(self, x):
        rev = 0
        dup_x = x
        while x > 0: 
            rev = rev * 10 + x % 10
            x /= 10
        return rev == dup_x
# note this solution in java could have overflow
# one can avoid it by doing x > 10 and return rev == dup_x / 10 and x == dup_x % 10
if __name__ == '__main__':
    sol = Solution1()
    print(sol.isPalindrome(int(sys.argv[1])))

        
