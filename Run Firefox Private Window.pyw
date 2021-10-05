import subprocess

if __name__ == '__main__':
	# firefoxExe = r'C:\Program Files\Mozilla Firefox\firefox.exe'
	firefoxExe = r'C:\Program Files\Firefox Developer Edition\firefox.exe'
	subprocess.run(f'{firefoxExe} -private-window')
