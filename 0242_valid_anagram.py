class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        for c in s:
            if c in dict_s: dict_s[c] += 1
            else: dict_s[c] = 1
        for c in t:
            if c in dict_t: dict_t[c] += 1
            else: dict_t[c] = 1
        return dict_s == dict_t

# awesome solution
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

# alphabet soltion
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        alphabet = {}
        for c in range(26):
            alphabet[chr(c + ord('a'))] = 0
        for c in s:
            alphabet[c] += 1
        for c in t:
            alphabet[c] -= 1
            if alphabet[c] < 0: return False
        return True

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
