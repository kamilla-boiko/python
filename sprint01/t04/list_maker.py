def list_maker(line, delim):
	if delim == '':
		delim = ' '
	lst = str.split(line, delim)
	return lst
