def read_file():
	with open('numbers.txt', 'r') as file:
		numbers = file.read().split(',')
		for num in numbers:
			print(num.strip())

if __name__ == '__main__':
	read_file()