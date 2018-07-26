class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[0:-1:2])


sol = Solution()
nums = [1,2,3,4]
print(sol.arrayPairSum(nums))