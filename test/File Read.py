if __name__ == '__main__':
	with open(r'R:\Temp\test.txt', mode='r', encoding='utf-8') as f:
		lines = f.readlines()
	for line in lines:
		print(line, end='')
