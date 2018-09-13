class Solution1(object):
    def shortestToChar(self, S, C):
    	# for each char store position of its left_e and right_e
    	c_dists = [[len(S),len(S)] for i in range(len(S))]
    	last_c_pos = -1
    	for i, char in enumerate(S):
    		if char == C: # update all distances between two e's
    			# handle this position:
    			c_dists[i] = [0,0]
    			for j in range(last_c_pos+1, i):
    				if last_c_pos == -1: # left boundary
    					c_dists[j][1] = i-j
    				else: 
    					c_dists[j] = [j-last_c_pos, i-j]
    			last_c_pos = i
    		elif i == len(S) - 1: # right boundary
    			for j in range(last_c_pos+1, i+1):
    				c_dists[j][0] = j-last_c_pos
    	ans = []
    	for dists in c_dists:
    		ans.append(min(dists))
    	return ans


class Solution(object):
    def shortestToChar(self, S, C):
    	c_dists = [len(S) for i in range(len(S))]
    	c_pos = -1
    	for i in range(len(S)):
    		if S[i] == C:
    			c_pos = i
    		if c_pos != -1:
    			c_dists[i] = i - c_pos
    	c_pos = -1
    	for i in range(len(S) - 1, -1, -1):
    		if S[i] == C:
    			c_pos = i
    		if c_pos != -1:
    			c_dists[i] = min(c_dists[i], c_pos - i)
    			
    	return c_dists

sol = Solution()
ans = sol.shortestToChar("loveleetcode",'e')
print(ans)
ans = sol.shortestToChar("aaba",'b')
print(ans)

