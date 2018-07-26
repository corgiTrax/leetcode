class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        hz, vt = 0, 0
        for m in moves:
        	if m == 'U': vt += 1
        	elif m == "D": vt -= 1
        	elif m == "L": hz += 1
        	elif m == "R": hz -= 1
        return hz == 0 and vt == 0	

class Solution1(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


sol = Solution1()
moves = "UUUUURRLLDDDDD"
print(sol.judgeCircle(moves))