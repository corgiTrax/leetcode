class Solution(object):
	def sortArrayByParity(self, A):
		head = 0
		tail = len(A) - 1
		while head < tail:
			if A[head] % 2 != 0 and A[tail] % 2 != 1:
				A[head], A[tail] = A[tail], A[head]
				head += 1
				tail -= 1
			elif A[head] % 2 == 0: #even number
				head += 1
			elif A[tail] % 2 == 1: #odd number
				tail -= 1
		return A

sol = Solution()
ans = sol.sortArrayByParity([1,3,2,4])
print(ans)
