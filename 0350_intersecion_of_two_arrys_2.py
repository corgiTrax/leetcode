import sys
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for item in nums1:
            if item not in dic: dic[item] = 1
            else: dic[item] += 1

        intersec = []
        for item in nums2:
            if item in dic:
                dic[item] -= 1
                if dic[item] >= 0: intersec.append(item)

        return intersec

sol = Solution()
print(sol.intersect([1,2,2,1],[2,2]))
