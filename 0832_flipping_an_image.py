class Solution(object):
    def flipAndInvertImage(self, A):
    	"""
    	:type A: List[List[int]]
    	:rtype: List[List[int]]
    	"""
    	dim = len(A[0])
    	for row in A:
    		for j in range(int(round(dim / float(2)))):
    			#print(j)
    			tmp = row[dim - j - 1]
    			row[dim - j - 1] = 1 - row[j]
    			row[j] = 1 - tmp
    	return A

sol = Solution()
ans = sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
print(ans)