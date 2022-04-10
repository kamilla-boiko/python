def get_anonymous(books):
	anonymous = []
	for book in books:
		if ' by ' not in book:
			anonymous.append(book)
	return anonymous
