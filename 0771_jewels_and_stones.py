class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = {}
        for j in J:
        	dic[j] = j
        count = 0
        for s in S:
        	if s in dic: count += 1
        return count

sol = Solution()
J = 'aA'
S = "aAAbbbb"
print(sol.numJewelsInStones(J,S))