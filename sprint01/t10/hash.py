import hashlib

def md5_hash(string):
	hash1 = hashlib.md5(string.encode())
	print(f'Original string: {string}')
	print('md5 hash generated is')
	print(hash1.hexdigest())

def sha1_hash(string):
	hash2 = hashlib.sha1(string.encode())
	print(f'Original string: {string}')
	print('sha1 hash generated is')
	print(hash2.hexdigest())
