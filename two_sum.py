#Solution 1: brute force, O(n^2), but this exceeds time limit
class Solution1:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        for i in range(len(num)):
            for j in range(len(num)):
                if i != j and num[i] + num[j] == target:
                    return i+1,j+1

#Then our solution is to use python dictionary, which is a hash table
#solution is O(n)
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hashed_num = {}
        for i in range(len(num)):
            hashed_num[num[i]] = i
        for i in range(len(num)):
            num_to_find = target - num[i]
            if num_to_find in hashed_num and i != hashed_num[num_to_find]:
                return i + 1, hashed_num[num_to_find] + 1


