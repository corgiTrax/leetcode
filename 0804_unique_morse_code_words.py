class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter_to_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes = []
        for w in words:
        	code = ''
        	for c in w:
        		code += letter_to_code[ord(c.lower()) - ord('a')]
        	codes.append(code)
        return len(set(codes))


sol = Solution()
words = ["gin", "zen", "gig", "msg"]
print(sol.uniqueMorseRepresentations(words))  
    