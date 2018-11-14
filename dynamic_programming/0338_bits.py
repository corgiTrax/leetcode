class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
      	num_ones = []
      	for n in range(num+1):
      		if n == 0:
      			num_ones.append(0)
      		elif n == 1:
      			num_ones.append(1)
      		else:
      			# divide ints into intervals depends on how many bits they have
      			interval = len(bin(n)[2:]) - 1
      			# position of the num in current interval
      			pos = n - 2 ** interval
      			ones = num_ones[pos] + 1
      			num_ones.append(ones)

        return num_ones

sol = Solution()
ans = sol.countBits(5)
print(ans)
