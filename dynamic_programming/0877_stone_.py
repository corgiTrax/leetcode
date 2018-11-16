class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        cache = {}
        def firstscore(l, r):
        	if l > r: return 0 
        	if l == r: return piles[l]
        	if (l,r) in cache: return cache[l,r]
        	score = max(piles[l] + min(firstscore(l+2, r), firstscore(l+1, r-1)),\
        		piles[r] + min(firstscore(l+1, r-1), firstscore(l, r-2)))
        	cache[l,r] = score
        	return score

        alexScore = firstscore(0, len(piles)-1)
        leeScore = sum(piles) - alexScore
        return alexScore > leeScore

sol = Solution()
ans = sol.stoneGame([5,3,4,5])
print(ans)