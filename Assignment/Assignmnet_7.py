def prefix_to_infix(prefix_expression):
  stack = []
  for token in reversed(prefix_expression):
    if token.isalpha():
      stack.append(token)
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()
      stack.append("( " + operand1 + token + operand2 + " )")
  return "".join(stack)


prefix_expression = "+A*BC"
infix_expression = prefix_to_infix(prefix_expression)
print(infix_expression)