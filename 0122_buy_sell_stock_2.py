class Solution1:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit


#An interesting question for stock, we actually only need to consider two adjacent prices, if it is fully known.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if prices == []: return profit
        #partition the prices array: find where it decreases
        partition_index = [0]
        for i in range(len(prices) - 1):
            if prices[i + 1] < prices[i]:
                partition_index.append(i)
        #append the last index, do a set to remove duplicates
        partition_index.append(len(prices)-1)
        partition_index = list(set(partition_index))
        #print(partition_index)
        for i in range(len(partition_index) - 1):
            buy_prices = prices[partition_index[i]:partition_index[i + 1]]
            if len(buy_prices) > 1:
                profit += max(0,prices[partition_index[i + 1]] - min(buy_prices))

        return profit

#The second solution exceeds time limit

prices = range(10001)
#prices.reverse()
sol = Solution()
print(sol.maxProfit(prices))
