#single number
#Solution1: count element, slightly more than linear time, need extra space
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        count = []
        min_num = min(A)
        if min_num >= 0:
            for i in range(max(A)+1):
                count.append(0) #to reduce search time later, count should indeed be a hash table
            for i in range(len(A)):
                count[A[i]] += 1
            for i in range(len(count)):
                if count[i] == 1:
                    return i
        if min_num < 0:
            num_count = abs(min_num) + 1 + max(A)           
            for i in range(num_count):
                count.append(0)
            for i in range(len(A)):
                count[A[i] + abs(min_num)] += 1
            for i in range(len(count)):
                if count[i] == 1:
                    return i - abs(min_num)
                

#Solution2: use bitwise XOR, if an element
class Solution2:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        answer = 0
        for i in range(len(A)):
            answer = answer ^ A[i]
        return answer

#interestingly, solution 1 is faster than solution 2.



