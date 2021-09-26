import os, glob, chardet

if __name__ == '__main__':
	# 텍스트 파일의 인코딩을 'UTF-8'로 변환
	for filePath in glob.glob(os.path.join(os.path.dirname(__file__), 'input/*')):
		fileContent = ''
		with open(filePath, 'rb') as f: # 인코딩 문제로 바이너리로 열어 인코딩 감지
			fileEncoding = chardet.detect(f.read())
		with open(filePath, 'r', encoding=fileEncoding['encoding']) as f:
			fileContent = f.read()
		with open(filePath, 'w', encoding='utf-8') as f:
			f.write(fileContent)
