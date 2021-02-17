import shutil, os

# 남은 용량 채우기
if __name__ == "__main__":
	fileList = [
		"00000004096",
		"00000102400",
		"00001048576",
		"00010485760",
		"00104857600",
		"01073741824",
		"10737418240"
	]
	os.makedirs("D:/Temp_Fill", exist_ok=True)
	for sourceFile in reversed(fileList):
		count = 1
		while shutil.disk_usage("D:").free >= os.path.getsize(sourceFile):
			copyFile = "D:/Temp_Fill/{} - {:0>2}".format(sourceFile, count)
			if not(os.path.isfile(copyFile)):
				shutil.copyfile(sourceFile, copyFile)
			count += 1


'''
00000004096
00000102400
00001048576
00010485760
00104857600
01073741824
10737418240
'''