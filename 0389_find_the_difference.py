class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for c in s:
            if c not in dic: dic[c] = 1
            else: dic[c] += 1
        for c in t:
            if c not in dic: return c
            else: 
                dic[c] -= 1
                if dic[c] < 0: return c
