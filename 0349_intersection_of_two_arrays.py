import sys

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for item in nums1:
            dic[item] = 0
        
        intersec = []
        for item in nums2:
            if item in dic and dic[item] == 0:
                dic[item] += 1
                intersec.append(item)
        return intersec

class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((set(nums1)).intersection(set(nums2)))

sol = Solution1()
print(sol.intersection([1,2,2,1], [2,2]))
