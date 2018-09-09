class Solution1(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if not nums:
			return 0
		for i,n in enumerate(nums):
			if n >= target:
				return i
		return len(nums)

class Solution(object):
	def searchInsert(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		# base case
		low, high = 0, len(nums) - 1
		while low <= high:
			mid = (low + high) / 2
			if nums[mid] == target: 
				return mid
			elif nums[mid] > target:
				high = mid - 1
			else:
				low = mid + 1
		return low 


sol = Solution1()
print(sol.searchInsert([1], 0))