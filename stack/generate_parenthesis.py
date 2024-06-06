'''
       add open parenthesis only if open <n
       add clsed parenthesis only if close < open
       valid if open = close = n
       ''' 

class Solution:

    def generateParenthesis(self, n: int) :
        stack =[]
        res =[]
        def backtrack(open, close):
            if open ==close==n:
                res.append("".join(stack))
                return

            if open <n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            if open > close:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()

        backtrack(0,0)
        return res

z = Solution()

print(z.generateParenthesis(4))

