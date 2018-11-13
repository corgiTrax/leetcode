class Solution(object):
	def maxProfit(self, prices):
		if prices == []: return 0
		min_price, max_prof = prices[0],0
		for i in range(1, len(prices)):
			if prices[i] < min_price:
				min_price = prices[i]
			elif prices[i] - min_price > max_prof:
				max_prof = prices[i] - min_price
		return max_prof

sol = Solution()
ans = sol.maxProfit([7,1,5,3,6,4])
print(ans)