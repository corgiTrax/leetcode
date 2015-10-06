# O(n^2) solution
class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]: return True
        return False

# python cheating solution
class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

# use hash or dictionary
class Solution(object):
    def containsDuplicate(self, nums):
        dict_num = {}
        for num in nums:
            if num in dict_num:
                return True
            else:
                dict_num[num] = 1
        return False


sol = Solution()
print(sol.containsDuplicate([0,1,2,3]))
