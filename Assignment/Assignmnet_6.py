def postfix_to_prefix(postfix_expression):
  stack = []
  for token in postfix_expression:
    if token.isalpha():
      stack.append(token)
    else:
      operand2 = stack.pop()
      operand1 = stack.pop()
      stack.append(token + operand1 + operand2)
  return "".join(stack)



postfix_expression = "AB*C+"
prefix_expression = postfix_to_prefix(postfix_expression)
print(prefix_expression)
