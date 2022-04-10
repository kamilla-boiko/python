def convert_to_bytes(str_int, str_bool, str_str):
	int_data = int(str_int)
	bool_data = True if str_bool == 'True' else False
	print(f'-- The int value is "{str_int}"')
	print(f'bytes: "{bytes(int_data)}"')
	print(f'-- The bool value is "{str(bool_data)}"')
	print(f'bytes: "{bytes(bool_data)}"')
	print(f'-- The string value is "{str_str}"')
	string = bytes(str_str, 'utf-8')
	print(f'bytes: "{string}"')
	print("---------------------")
