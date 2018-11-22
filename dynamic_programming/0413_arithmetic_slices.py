# Note: a TLE solutioj
class Solution1(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        # table[i][j] indicate whether A[i:j+1] is an arithmetic slice
        table = [[False for j in range(len(A))] for i in range(len(A)-3+1)]
        # base case: slices of len 3
        for i in range(len(A)-3+1):
        	if A[i+1] - A[i] == A[i+2] - A[i+1]: 
        		table[i][i+2] = True
        		count += 1

        for l in range(4, len(A)+1): # length of all possible slices
        	for i in range(0, len(A) - l + 1):
        		j = i + l - 1
        		if table[i][j-1] == True and A[j] - A[j-1] == A[j-1] - A[j-2]:
        			table[i][j] = True
        			count += 1 
        return count

# intuition: say 0,1,2,3 contains 2 *new* slices from 0,1,2, what if we add 4? how many new slices do we introduce?
# it is 2 + 1, since the new ones adding 4 can be constructed from the 2 new ones when adding 3, plus 2,3,4
# so every dp[i] = dp[i-1] + 1, counting how many new slices are introduced
class Solution2(object):
    def numberOfArithmeticSlices(self, A):
    	count = 0
    	dp = [0 for i in range(len(A))]
    	for i in range(2, len(A)):
    		if A[i] - A[i-1] == A[i-1] - A[i-2]:
    			dp[i] = dp[i-1] + 1
    			count += dp[i]
    	return count


sol = Solution2()
A = [1,2,3,4,5,6,7,5,4,3,24,1,24,1,2,3,4,5,1,3,4,5,7,9]
ans = sol.numberOfArithmeticSlices(A)
print(ans)