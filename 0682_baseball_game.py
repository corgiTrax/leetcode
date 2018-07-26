class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        point = 0
        last = [] # last three valid points
        for op in ops:
        	if op == '+':
        		pt = last[-1] + last[-2]
        		point += pt
        		last.append(pt)
        	elif op == 'D':
        		pt = (last[-1] * 2)
        		point += pt
        		last.append(pt)
        	elif op == 'C':
        		pt = last.pop()
        		point -= pt
        	else:
        		point += int(op)
        		last.append(int(op))
        return point


sol = Solution()
ops = ['5','2','C','D','+']
print(sol.calPoints(ops))