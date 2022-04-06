print("---- Simple calculator ----")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter sign of operation: ")
if not (num1.isnumeric() and num2.isnumeric()):
    print("usage: this script sequentially reads two integers, but not string")
else:
    num1 = int(num1)
    num2 = int(num2)
    if operator == '*':
        print(f"{num1} {operator} {num2} = {num1 * num2}")
    elif operator == '-':
        print(f"{num1} {operator} {num2} = {num1 - num2}")
    elif operator == '+':
        print(f"{num1} {operator} {num2} = {num1 + num2}")
    elif operator == '/':
        print(f"{num1} {operator} {num2} = {num1 / num2}")
    else:
        print("usage: the operator must be '*' or '+' or '-' or '/’")
print("---- Simple calculator ----")