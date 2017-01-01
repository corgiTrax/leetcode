class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # note the no extra space constraint
        num_range = len(nums) # [1,n]
        mark = [1] * (num_range + 1)
        for i in nums:
            mark[i] = 0
        return [i for i in range(1, len(mark)) if mark[i] == 1]

class Solution1(object):
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))

class Solution2(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

if __name__ == '__main__':
    array = [4,3,2,7,8,2,3,1]
    sol = Solution1()
    print(sol.findDisappearedNumbers(array))
