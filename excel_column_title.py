#Simply base-10 to base-26 
class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num <= 26:
            return self.num_to_char(num)
        else:
            return self.convertToTitle((num -1)/26) + self.num_to_char(num % 26)

    def num_to_char(self, number):
        #1 = A, 2 = B, ... , 26 = Z
        if number == 0:
            return 'Z'
        else:
            return chr(number + ord('A') - 1)
       
#The only tricky thing is that excel column starts at 1, not 0. 
