command = input("Please, choose command: ")
if command != "find" and command != "concat" and command != "beatbox":
	print("usage: command find | concat | beatbox")
else:
	s1 = input("Please, enter first string: ")
	s2 = input("Please, enter second string: ")
	if command == "find":
		print(s1 in s2)
	elif command == "concat":
		print(f"Your string is: {s1 + s2}")
	else:
		num1 = input("Please, enter first number: ")
		num2 = input("Please, enter second number: ")
		if not (num1.isnumeric() and num2.isnumeric()):
			print("usage: first and second beatbox numbers must be integer or float, but string")
		else:
			print(f"{s1 * int(num1)}")
			print(f"{s2 * int(num2)}")
