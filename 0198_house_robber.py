# recursive solution, slow
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])
        elif len(nums) == 3: return max(nums[1], nums[0] + nums[2])
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

# dynamic programming, fasti; notice why dp is faster than recursion: a lot of computation is done but not stored
class Solution(object):
    def rob(self, nums):
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        results = {}
        results[0] = nums[0] # first house
        results[1] = max(nums[0], nums[1]) # first two houses

        for i in range(2,len(nums)):
            results[i] = max(results[i-1], results[i-2] + nums[i]) # note this step

        return results[len(nums) - 1]

sol = Solution()
print(sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
