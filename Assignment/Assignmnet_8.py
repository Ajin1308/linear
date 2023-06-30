def check_brackets(code):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in code:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or bracket_pairs[stack.pop()] != char:
                return False

    return len(stack) == 0


code_snippet = "{[()()]}"
print(check_brackets(code_snippet))
