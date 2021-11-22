import string, random, tkinter as tk
from tkinter import ttk, scrolledtext


if __name__ == '__main__':
	numberAlphabetLetters =  string.digits + string.ascii_letters

	def getRandomString(length):
		result = ''
		for i in range(length):
			result += random.choice(numberAlphabetLetters)
		return result
	
	def setTextWidget1(inputString):
		textWidget1.delete(1.0, tk.END)
		textWidget1.insert(1.0, inputString)

	root = tk.Tk()
	frame = ttk.Frame(root, padding=10)
	frame.grid()
	text1 = tk.StringVar()
	text1.set(20)
	textWidget1 = scrolledtext.ScrolledText(frame, width=20, height=5)
	textWidget1.grid(column=0, row=0)
	ttk.Spinbox(frame, textvariable=text1, from_=1, to=10000, width=5, justify="right").grid(column=0, row=1)
	ttk.Button(frame, text='get', command=lambda: setTextWidget1(getRandomString( int(text1.get()) ))).grid(column=0, row=2)

	root.eval('tk::PlaceWindow . center')
	root.mainloop()
