import sys

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            if c not in dic: dic[c] = 1
            else: dic[c] += 1

        has_odd = num_even = 0

        for c in dic:
            if dic[c] % 2 == 0: num_even += dic[c]
            elif dic[c] >= 3: 
                num_even += dic[c] - 1
                has_odd = 1
            else: has_odd = 1

        return num_even + has_odd

class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ct = 0
        for c in s:
            if c not in dic: dic[c] = 1
            else: dic[c] += 1
            if dic[c] == 2: 
                ct += 2
                del dic[c]
        return bool(dic) + ct

sol = Solution()
print(sol.longestPalindrome(sys.argv[1]))
