import sys

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ["0"] * len(s)
        for i,c in enumerate(s):
            r[len(s) - 1 - i] = c
        return "".join(r)

#note: if you attempt to use += for join the string in python, it's too slow
class Solution3(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        for i in range(len(s) - 1, -1, -1):
            r += s[i]
        return r

if __name__ == '__main__':
    sol = Solution3()
    print(sol.reverseString(sys.argv[1]))
        
