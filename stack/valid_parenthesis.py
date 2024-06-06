def valid_parenthesis(expression):
    opened = {'(', '{', '['}
    closed = {')', '}', ']'}
    stack = []

    for char in expression:
        if char in opened:
            stack.append(char)
        elif char in closed:
            if not stack:
                return False
            top_char = stack.pop()
            if not is_balanced(top_char,char):
                return False
    return  True if not stack else False
    
def is_balanced(open, closed):
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    return bracket_pairs[closed]==open


expression = "{(a+b)+(c+d)}"

print(valid_parenthesis(expression))
    


