import sys
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_swap_index = len(s)
        vowels = {'a':1,'e':1,'i':1,'o':1,'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        s_list = list(s)
        for i in range(len(s_list)):
            if i == last_swap_index: return "".join(s_list)
            elif s_list[i] in vowels:
                for j in range(last_swap_index - 1, i-1, -1):
                    if j == i: return "".join(s_list)
                    elif s_list[j] in vowels:
                        temp = s_list[j]
                        s_list[j] = s_list[i]
                        s_list[i] = temp
                        last_swap_index = j
                        break
        return "".join(s_list)

class Solution1(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_dict = {'a':1,'e':1,'i':1,'o':1,'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        vowel_index = []
        vowels = []
        s_list = list(s)
        for i,c in enumerate(s_list):
            if c in vowel_dict:
                vowel_index.append(i)
                vowels.append(c)
        ct = len(vowels)
        for i in range(ct):
            s_list[vowel_index[i]] = vowels[ct - 1 - i]

        return "".join(s_list)

class Solution2(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a':1,'e':1,'i':1,'o':1,'u':1, 'A':1, 'E':1, 'I':1, 'O':1, 'U':1}
        s_list = list(s)
        start = 0; end = len(s_list) - 1
        while start < end:
            while start < end and not(s_list[start] in vowels): start += 1
            while start < end and not(s_list[end] in vowels): end -= 1
            
            temp = s_list[start]
            s_list[start] = s_list[end]
            s_list[end] = temp
        
            start += 1; end -=1
        return "".join(s_list)

if __name__ == '__main__':
    sol = Solution2()
    print(sol.reverseVowels(sys.argv[1]))
