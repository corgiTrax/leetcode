class Solution:
    # @return an integer
    #there's an overflow issue, integers are assumed to be 32bit, but in python this is not a problem
    #The tricky thing is that the input can be alright, but reverse overflows
    def reverse(self, x):
        str_x = str(x)
        if x < 0:
            reverse_str_x = str_x[0] + (str_x[1::])[::-1]
        else:
            reverse_str_x = str_x[::-1]
        
        reverse_x = int(reverse_str_x)
        if reverse_x < -2**32/2 or reverse_x > 2**32/2 - 1:
            return 0

        return int(reverse_str_x)

sol = Solution()
print(sol.reverse(-127663))        
