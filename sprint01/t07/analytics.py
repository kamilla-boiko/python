import string

def print_str_analytics(line):
	printable = 0
	alphanumeric = 0
	alphabetic = 0
	decimal = 0
	lowercase = 0 
	uppercase = 0
	whitespace = 0
	for character in line:
		if character.isprintable():
			printable += 1
		if character.isalnum():
			alphanumeric += 1
		if character.isalpha():
			alphabetic += 1
		if character.isnumeric():
			decimal += 1
		if character.islower():
			lowercase += 1
		if character.isupper():
			uppercase += 1
		if character.isspace():
			whitespace += 1
	
	print('|------------------------------------------------|')
	print('|                String analytics                |')
	print('|------------------------------------------------|')
	print(f"| '{line}'")
	print('|------------------------------------------------|')
	print(f"| Number of printable characters is: {printable}")
	print(f"| Number of alphanumeric characters is: {alphanumeric}")
	print(f"| Number of alphabetic characters is: {alphabetic}")
	print(f"| Number of decimal characters is: {decimal}")
	print(f"| Number of lowercase letters is: {lowercase}")
	print(f"| Number of uppercase letters is: {uppercase}")
	print(f"| Number of whitespace characters is: {whitespace}")
	print('|------------------------------------------------|')
