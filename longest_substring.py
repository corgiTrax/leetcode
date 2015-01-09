'''This is standard O(n^2) solution'''
class Solution1:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
#        print(s, len(s))
        max_length = 0
        for i in range(len(s)):
            hashed_char = {}
            sub_s = s[i::]
            #if current max_length is greater than the rest, break
            if max_length >= len(sub_s): break
            for j in range(len(sub_s)):
                if sub_s[j] in hashed_char:
                    max_length = max(len(hashed_char), max_length)
#                   print(hashed_char)
                    break
                else:
                    hashed_char[sub_s[j]] = 0
                    if j == len(sub_s) - 1: # we reach the end
                        max_length = max(len(hashed_char), max_length)
                       
        return max_length

'''A slightly faster solution but not good enough'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        while start < len(s):
            hashed_char = {}
            sub_s = s[start::]
            if max_length >= len(sub_s): break
            for i in range(len(sub_s)):
                if sub_s[i] in hashed_char:
                    max_length = max(len(hashed_char), max_length)
                    start = start + hashed_char[sub_s[i]] + 1
                    break
                else:
                    hashed_char[sub_s[i]] = i
                    if i == len(sub_s) - 1: # we reach the end
                        max_length = max(len(hashed_char), max_length)
                        return max_length
                       
        return max_length

'''A better O(n) solution'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        hashed_char = {}
        max_length = 0 
        start = end = 0

        while end < len(s):
            if s[end] in hashed_char and hashed_char[s[end]] >= start:
                start = hashed_char[s[end]] + 1

            hashed_char[s[end]] = end
            end += 1
            
            max_length = max(maxlength, end - start)

        return max_length  

sol = Solution()
print(sol.lengthOfLongestSubstring("""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"""))
