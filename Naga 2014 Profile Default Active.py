import glob, xml.etree.ElementTree as ET, os
from tkinter import messagebox

if __name__ == '__main__':
	for filePath in glob.glob(r'C:\ProgramData\Razer\Synapse\Accounts\AM_*\Devices\Naga 2014\Profiles\*.xml'):
		# with open(filePath, 'r') as file:
		# 	print(file.read())
		# with open(filePath + '.tmp', 'w') as file:
		# 	pass

		tree = ET.parse(filePath)
		root = tree.getroot()
		isEdited = False
		if root.find('ProfileName').text.find('01') == 0:
			if root.find('Active').text == '0':
				root.find('Active').text = '1'
				isEdited = True
		else:
			if root.find('Active').text == '1':
				root.find('Active').text = '0'
				isEdited = True
		if isEdited:
			print(filePath)
			try:
				os.rename(filePath, filePath + '.tmp')
				tree.write(filePath)
				os.remove(filePath + '.tmp')
			except Exception as e:
				messagebox.showerror(title=__file__, message=str(e))
