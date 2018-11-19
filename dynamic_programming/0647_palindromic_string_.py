import copy
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        palind_set = []
        count = 0
        # get palind substring of length 1 and 2
        palind_len_1, palind_len_2 = [], []
        for i in range(len(s)):
        	palind_len_1.append((i,i))
        	count += 1
        	if i != len(s) - 1:
        		if s[i] == s[i+1]: 
        			palind_len_2.append((i,i+1))
        			count += 1
        palind_set.append(palind_len_1)
        palind_set.append(palind_len_2)

        for l in range(3, len(s)+1):
        	palind_len_l = []
        	prev_l_index = l - 2 - 1 # the current subl is formed by previous ones
        	for sub_palind in palind_set[prev_l_index]:
        		left = sub_palind[0] - 1
        		right = sub_palind[1] + 1
        		if  left >= 0 and  right <= len(s) - 1 and s[left] == s[right]:
        			palind_len_l.append((left, right))
        			count += 1
        	palind_set.append(copy.deepcopy(palind_len_l))

        return count

sol = Solution()
s = 'aaa'
ans = sol.countSubstrings(s)
print(ans)

# hint: next time: use a 2D table [i][j] to indicate whether s[i:j] is a palind        
