class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dicS = {}
        for c in secret:
            if c not in dicS: dicS[c] = 1
            else: dicS[c] += 1
        A = B = 0
        checked = []
        for i, c in enumerate(guess):
            if c == secret[i]: 
                A += 1
                dicS[c] -= 1
                checked.append(True)
            else: checked.append(False)
        for i, c in enumerate(guess):
            if c in dicS and dicS[c] > 0 and not checked[i]: 
                B += 1
                dicS[c] -= 1
        return str(A) + 'A' + str(B) + 'B'
