# v1.0.0.20220616
# 윈도우 파일명 위반 문자 교체
def fileNameFilter(string, replacementString):
	filterCharacters = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', '"', '*', '/', ':', '<', '>', '?', '\\', '|']
	result = string
	for oldChar in filterCharacters:
		result = result.replace(oldChar, replacementString)
	return result

if __name__ == '__main__':
	print(fileNameFilter('\"t\te\ns\tt\"', '_'))
