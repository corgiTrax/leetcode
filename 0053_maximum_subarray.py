class Solution1(object):
	'''O(n^2) solution'''
	def maxSubArray(self, nums):
		sums = []
		for start_index in range(0, len(nums) + 1):
			for end_index in range(start_index + 1, len(nums) + 1):
				cur_array = nums[start_index:end_index]
				print(start_index, end_index, cur_array)
				sums.append(sum(cur_array))
		return max(sums)


class Solution(object):
	def maxSubArray(self, nums):
		for i in range(1, len(nums)):
			if nums[i - 1] > 0: nums[i] += nums[i - 1]
		return max(nums)

sol = Solution()
ans = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(ans)