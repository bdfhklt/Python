# 두 set 차이
if __name__ == '__main__':
	TARGET_PATH1 = r'E:\Temp\fileList1.txt'
	TARGET_PATH2 = r'E:\Temp\fileList2.txt'

	list1 = None
	list2 = None
	set1 = set()
	set2 = set()

	with open(TARGET_PATH1, 'r') as f:
		for line in f.readlines():
			set1.add(line.strip())
	with open(TARGET_PATH2, 'r') as f:
		for line in f.readlines():
			set2.add(line.strip())

	print('set1')
	print(set1.difference(set2))
	print('set2')
	print(set2.difference(set1))
