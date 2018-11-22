# Note: draw the matrix dp!!
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        l1, l2 = len(s1), len(s2)
        # sol for s1[0:i) and s2[0:j), note not including i,j
        dp = [[0 for j in range(l2+1)] for i in range(l1+1)]
        
        # initialize first row so j-1 can be calculated
        for j in range(1, l2+1):
        	dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, l1+1):
        	dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        	for j in range(1, l2+1):
        		if s1[i-1] == s2[j-1]:
        			dp[i][j] = dp[i-1][j-1]
        		else:
        			dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

        return dp[l1][l2]

sol = Solution()
ans = sol.minimumDeleteSum("delete", "leet")
print(ans)