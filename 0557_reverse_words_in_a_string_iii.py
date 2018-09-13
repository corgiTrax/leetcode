class Solution(object):
	def reverseWords(self, s):
		tmp = ans = ''
		for i, l in enumerate(s):
			if i == len(s) - 1:
				tmp += l
				ans += tmp[::-1]
			elif l == ' ':
				ans += tmp[::-1]
				ans += ' '
				tmp = ''
			else:
				tmp += l
		return ans
		# return " ".join(x[::-1] for x in s.split())

sol = Solution()
ans = sol.reverseWords("Let's take LeetCode contest")
print(ans)