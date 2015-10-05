class Solution(object):
    def romanToInt(self, s):
        roman_to_int_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        numbers = []
        for c in s:
            numbers.append(roman_to_int_dict[c])
        num = 0
        for i in range(len(numbers)):
            if (i != len(numbers) - 1) and (numbers[i] < numbers[i + 1]):
                num -= numbers[i]
            else:
                num += numbers[i]
        return num


sol = Solution()
print(sol.romanToInt("IV"))
            
