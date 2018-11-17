class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        num_row = len(A)
        num_col = len(A[0])
        if num_row == 0: return 0
        for i in range(num_row-2, -1, -1):
        	for j in range(num_col):
        		A[i][j] += min(A[i+1][max(0,j-1)], A[i+1][j], A[i+1][min(j+1, num_col-1)])
        return min(A[0])

sol = Solution()
ans = sol.minFallingPathSum([[]])
print(ans)


