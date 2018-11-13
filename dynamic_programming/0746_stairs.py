class Solution(object):
	def minCostClimbingStairs(self, cost):
		for i in range(len(cost) - 3, -1, -1):
			cost[i] = cost[i] + min(cost[i+1], cost[i+2])
		return min(cost[0], cost[1])


sol = Solution()
ans1 = sol.minCostClimbingStairs([10,15,20])
ans2 = sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(ans1, ans2)