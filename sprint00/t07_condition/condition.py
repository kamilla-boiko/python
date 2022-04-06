answer = input('There are 3 signs in front of you. Which one would you like to read? ')
if answer == 'right':
	print('The right sign says: "DEAD PEOPLE ONLY"')
elif answer == 'left':
	print('The left sign says: "BEWARE!"')
elif answer == 'middle':
	print('The middle sign says: "CERTAIN DEATH"')
else:
	print(f'There is no {answer} sign')