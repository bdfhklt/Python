import os, glob

if __name__ == "__main__":
	print()
	for filePath in glob.glob(os.path.join(os.path.dirname(__file__), 'input/*')):
		fileContent = ''
		with open(filePath, 'r') as f:
			fileContent = f.read()
		with open(filePath, 'w', encoding='utf-8') as f:
			f.write(fileContent)
