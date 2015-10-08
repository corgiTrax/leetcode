class Solution(object):
    def removeElement(self, nums, val):
        for num in nums[:]: # iterate through a copy of nums, note that you can't iterate through the original one
            if num == val:
                nums.remove(num)
        return len(nums)

sol = Solution()
print(sol.removeElement([4,5],4))
