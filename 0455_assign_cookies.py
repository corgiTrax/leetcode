# TLE solution
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        # for each child find min size that is goe to her content
        for cont in g:
            min_size = 'na'
            min_index = -1
            for i, size in enumerate(s):
                if size >= cont and (min_size == 'na' or size < min_size): 
                    min_size = size
                    min_index = i
                if min_size == cont: break
            if min_index != -1:
                del s[min_index]
                count += 1
        return count

# use sort
class Solution1(object):
    def findContentChildren(self, g, s):
        if len(s) == 0 or len(g) == 0: return 0
        g.sort()
        s.sort()
        count = 0
        index = 0
        for cont in g:
            for i in range(index, len(s)):
                if s[i] >= cont: 
                    count += 1
                    index = i + 1
                    break
            if index == len(s):
                break
        return count

class Solution2(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        index = 0
        count = 0
        for i, size in enumerate(s):
            if index == len(g): break
            if size >= g[index]:
                count += 1
                index += 1
        return count


if __name__ == '__main__':
    sol = Solution2()
    print(sol.findContentChildren([10,9,8,7,10,9,8,7],[10,9,8,7]))
