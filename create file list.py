import glob, os

# 파일 리스트 생성
if __name__ == '__main__':
	# '**/*': 모든 하위 항목
	TARGET_PATH = r'E:\Temp'
	TARGET_TYPE = '**\\*'
	
	fileList = ''

	# print(os.path.join(TARGET_PATH, TARGET_TYPE))
	for entry in glob.glob(os.path.join(TARGET_PATH, TARGET_TYPE), recursive=True):
		if os.path.isfile(entry):
			fileList += entry + '\n'
	fileList = fileList.strip()
	# print(fileList)
	
	with open(os.path.join(os.path.dirname(__file__), 'fileList.txt'), 'w') as f:
		f.write(fileList)
