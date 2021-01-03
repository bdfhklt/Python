import re

for i in range(1,26):
	with open('EP{0}.smi'.format(repr(i).zfill(2)), 'r') as f1:
		result = ''
		line = True
		while line:
			line = f1.readline()
			# print(line)
			t1 = re.search('Start=\d+', line)
			if t1:
				t1 = t1.group()
				t2 = re.search('\d+', t1).group()
				line = re.sub(t1, 'Start=' + str(int(t2) + 1000), line)
				# print(t1.group())
				# print(t2)
				# print(line)
			result += line
		# print(result)
	with open('EP{0}.smi'.format(repr(i).zfill(2)), 'w') as f2:
		f2.write(result)