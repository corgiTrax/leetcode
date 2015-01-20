class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if stack == []: last = None
                else: last = stack.pop()
                if char == ')' and last != '(': return False
                if char == ']' and last != '[': return False
                if char == '}' and last != '{': return False
        
        return stack == []

