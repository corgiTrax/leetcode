class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        ascA = ord('A')
        ascZ = ord('Z')
        ascDiff = ord('a') - ord('A')
        for c in str[:]:
        	if  ascA <= ord(c) <= ascZ:
        		c = chr(ord(c) + ascDiff)
        	res += c
        return res


sol = Solution()
import sys
print(sol.toLowerCase(sys.argv[1]))