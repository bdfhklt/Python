# import tkinter.filedialog

if __name__ == "__main__":
	with open("C:\Google Drive\info\Moe info.txt", mode="r", encoding="utf-8") as f:
		lines = f.readlines()
	for line in lines:
		print(line, end="")
