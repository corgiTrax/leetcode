class Solution(object):
    def moveZeroes(self, nums):
        for num in nums[:]: #iterate through a copy of nums
            if num == 0:
                nums.remove(num)
                nums.append(0) 

class Solution2(object):
    def moveZeroes(self, nums):
        count_zero = 0
        i = 0
        while i < len(nums):
            print(i)
            if nums[i] == 0:
                nums.remove(nums[i])
                if count_zero == 0:
                    nums.append('z')
                else:
                    nums.append(0)
                i -= 1
                count_zero += 1 
            elif nums[i] == 'z': #notiice! this MUST be elif, because the above nums[i] is a pointer to 'z' 
                nums[i] = 0
                break  
            i += 1
        
        print(nums)


sol = Solution2()
sol.moveZeroes([0,1,2,3,4])


