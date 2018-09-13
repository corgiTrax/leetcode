class Solution(object):
    def findMaxAverage(self, nums, k):
    	"""
    	:type nums: List[int]
    	:type k: int
    	:rtype: float
    	"""
    	cur_sum = sum(nums[0:k])
    	max_sum = cur_sum
    	for i in range(k, len(nums)):
    		cur_sum = cur_sum - nums[i - k] + nums[i]
    		if cur_sum > max_sum:
    			max_sum = cur_sum

    	return max_sum / float(k)

sol = Solution()
ans = sol.findMaxAverage([1,12,-5,-6,50,3], 4)
print(ans) 