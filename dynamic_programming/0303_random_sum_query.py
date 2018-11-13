class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        cur_sum = 0
        self.sums = [] # store sum from 0:i
        for i in range(len(nums)):
            cur_sum += nums[i] 
            self.sums.append(cur_sum)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0: return self.sums[j]
        else: return self.sums[j] - self.sums[i-1]

        

# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
print(param_1)