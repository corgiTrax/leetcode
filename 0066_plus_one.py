class Solution1:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        number = 0
        for i in range(len(digits)):
            number += digits[i] * (10**(len(digits) - i - 1))
        number += 1
        print(number) 
        char_number = str(number)
        new_digits = [int(char) for char in char_number]

        return new_digits

#A better solution
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9: digits[i] = 0 
            else: 
                digits[i] += 1
                return digits

        digits[0] = 0
        digits.insert(0, 1)
        return digits
            


sol = Solution()
print(sol.plusOne([3,4,2,1,5,6,7]))
