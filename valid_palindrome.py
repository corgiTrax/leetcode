class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if s == '':
            return True
        else:
            #remove all non alphabetical characters
            new_s = ''
            for char in s:
                if (ord(char) >= ord('A') and ord(char) <= ord('Z')) \
                    or (ord(char) >= ord('a') and ord(char) <= ord('z')) \
                    or (ord(char) >= ord('0') and ord(char) <= ord('9')):
                    new_s += char
            #to lower case
            new_s = new_s.lower()
            #reverse
            new_s_reversed = new_s[::-1]
            return new_s_reversed == new_s


#A much simpler solution
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = filter(s.isalnum, s.lower())
        return s == s[::-1]

''' filter(function, iterable)
    Construct a list from those elements of iterable for which function returns true. 
iterable may be either a sequence, a container which supports iteration, or an iterator. 
If iterable is a string or a tuple, the result also has that type; otherwise it is always a list. 
If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed.'''       
