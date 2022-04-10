def validator(arg):
	expression = str.split(arg, ' ')

	if len(expression) < 3:
		return False

	try:
		num1 = float(expression[0])
		num2 = float(expression[2])
		op = expression[1]
		if op != '>' and op != '<' and op != '>=' and op != '<=' and op != '==':
		   return False
	except ValueError:
		return False

	if (op == '>') and (num1 < num2):
		return f"{num1} < {num2}"
	if op == '<' and (num1 > num2):
		return f"{num1} > {num2}"
	if op == '==' and (num1 != num2):
		if num1 <= num2:
			return f"{num1} <= {num2}"
		else:
			return f"{num1} >= {num2}"
	if op == '<=' and (num1 >= num2):
		if num1 == num2:
			return f"{num1} == {num2}"
		else:
			return f"{num1} >= {num2}"
	if op == '>=' and (num1 <= num2):
		if num1 == num2:
			return f"{num1} == {num2}"
		else:
			return f"{num1} <= {num2}"
	else:
		return True
