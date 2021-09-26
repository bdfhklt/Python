import tkinter.filedialog

if __name__ == '__main__':
	tmp1 = tkinter.filedialog.askopenfile()
	print(tmp1.name)
	pass
