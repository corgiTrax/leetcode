#Solution 1: shortest solution
#simply sort and return the middle number
#but this takes O(nlogn) time

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        return sorted(num)[len(num)/2]

#Solution 2: Prof.Moore's majority voting algorithm (utexas) 
#this is a very smart algorithm, O(n) time and O(1) space
#basic idea is that if majority element exists, we can cancel out votes and majority element will still win
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate = 0
        count = 0
        for i in range(len(num)):
            if count == 0:
                candidate = num[i]
                count += 1
            elif candidate == num[i]:
                count += 1
            else: 
                count -= 1
        return candidate 
