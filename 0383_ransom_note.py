import sys
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = {}
        for c in magazine:
            if c not in dic: dic[c] = 1
            else: dic[c] += 1
        for c in ransomNote:
            if c not in dic or dic[c] == 0: return False
            else: dic[c] -= 1
        return True

if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct(sys.argv[1], sys.argv[2]))
