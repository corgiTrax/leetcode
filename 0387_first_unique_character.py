import sys
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for pos,c in enumerate(s):
            if c not in dic: dic[c] = [1, pos]
            else: dic[c][0] += 1
        first = len(s) 
        for c in dic:
            if dic[c][0] == 1:
                if dic[c][1] < first: first = dic[c][1]
        if first == len(s): return -1
        else: return first

if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar(sys.argv[1]))
        
