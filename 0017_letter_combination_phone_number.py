import sys
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return ""
        book = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        combs = [""]

        for num in digits:
            new_combs = [] # store combinations after adding one more digit
            for n in range(len(combs)):
                prefix = combs[n]
                for k in book[num]:
                    new_combs.append(prefix + k)
            combs = new_combs
        return combs

# a depth first search approach needs to be reviewed

if __name__ == '__main__':
    sol = Solution()
    print(sol.letterCombinations(sys.argv[1]))
