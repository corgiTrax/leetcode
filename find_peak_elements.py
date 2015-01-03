class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        for i in range(len(num)):
            if i == 0:
                if len(num) == 1:
                    return i
                if num[i] > num[i + 1]:
                    return i
            elif i == len(num) - 1:
                if num[i] > num[i - 1]:
                    return i
            else:
                if num[i] > num[i -1] and num[i] > num[i + 1]:
                    return i
            

'''Desired solution requires O(logn): this is possible using binary search even with 
unsorted arrays. Since you only have to find any peak, if the left or right side is bigger than the current pivot, 
look at that half of the array for a peak since it is guaranteed there will be one on that side. 
This is because there is an increase in elevation detected on that side and at the very least, 
the end of the array is a decrease (-infinity at both end). Also n[i] != n[i+1]'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        left = 0 
        right = len(num) - 1
        
        while left <= right:
            mid = (left + right)/2
                        
            if mid - 1 == -1: mid_left = float('-inf')
            else: mid_left = num[mid - 1]
            if mid + 1 == len(num): mid_right = float('-inf')
            else: mid_right = num[mid + 1]
           
            if num[mid] > mid_left and num[mid] > mid_right:
                return mid

            elif num[mid] < mid_left:
                '''search for peak in left half'''
                right = mid - 1
            else:
                '''search for peak in right half'''
                left = mid + 1
                         
          

            
