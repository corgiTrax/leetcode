class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i,num in enumerate(nums):
            if num not in dic: dic[num] = i
            else:
                if i - dic[num] <= k: return True
                else: dic[num] = i
        return False
