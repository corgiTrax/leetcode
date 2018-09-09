class Solution(object):
	def pivotIndex(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		leftsum = 0 
		rightsum = sum(nums) 
		for i in range(len(nums)):
			rightsum -= nums[i]
			if leftsum == rightsum:
				return i
			leftsum += nums[i]
		return -1

sol = Solution()
ans = sol.pivotIndex([1,7,3,6,5,6])
print(ans)