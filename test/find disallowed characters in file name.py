import os

# 파일명에서 불허하는 문자들 찾기
if __name__ == '__main__':
	DIR_FULL_PATH = r'R:\Temp'

	chr100List = []
	chr100 = ''
	for i in range(0x0, 0x110000):
		chr100 += chr(i)

		if len(chr100) == 100:
			chr100List.append(chr100)
			chr100 = ''
	chr100 += '123456789'
	chr100List.append(chr100)

	exceptionChrs = ''

	for _chr100 in chr100List:
		file1FullPath = os.path.join(DIR_FULL_PATH, f'0{_chr100}.txt')
		try:
			with open(file1FullPath, 'w', encoding='utf-8') as f:
				f.write('')
			os.remove(file1FullPath)
		except:
			for chr1 in _chr100:
				file2FullPath = os.path.join(DIR_FULL_PATH, f'0123456789{chr1}0123456789.txt')
				try:
					with open(file2FullPath, 'w', encoding='utf-8') as f:
						f.write('')
						file2Writed = True
					fileCount1 = len(os.listdir(DIR_FULL_PATH))
					os.remove(file2FullPath)
					fileCount2 = len(os.listdir(DIR_FULL_PATH))
					if fileCount1 == fileCount2: # 파일 삭제 안되면
						exceptionChrs += chr1
				except:
					exceptionChrs += chr1

	# resultFileFullPath = os.path.join(DIR_FULL_PATH, 'exceptionChrs.txt')
	# with open(resultFileFullPath, 'w', encoding='utf-8') as f:
	# 	f.write(exceptionChrs)
	print([i for i in exceptionChrs])
	'''
	result(count: 41): unicode 0 ~ 31(0 ~ 0x1f) "*/:<>?\|
	['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', '"', '*', '/', ':', '<', '>', '?', '\\', '|']
	'''
