def add_to_bookshelf(book_to_add, bookshelf):
	count = 0
	while count < len(bookshelf):
		if bookshelf[count] == '---':
			bookshelf[count] = book_to_add
			return True
		count += 1
	return False
