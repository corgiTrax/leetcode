import sys
import copy

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        new_matrix = []
        flatten_nums = []
        for row in nums:
            flatten_nums += row
        new_row = []
        for i, item in enumerate(flatten_nums):
            new_row.append(item)
            if (i+1) % c == 0:
                new_matrix.append(copy.deepcopy(new_row))
                new_row = []
        return new_matrix

class Solution1(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        new_matrix = []
        new_row = []
        ct = 0
        for i, row in enumerate(nums):
            for j, item in enumerate(row):
                new_row.append(item)
                ct += 1
                if ct % c == 0:
                    new_matrix.append(copy.deepcopy(new_row))
                    new_row = []
        return new_matrix


sol = Solution1()
matrix = [[1,2,3], [4,5,6]]
r = int(sys.argv[1])
c = int(sys.argv[2])
print(sol.matrixReshape(matrix, r, c))
