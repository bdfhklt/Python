import os, subprocess, winsound

if __name__ == '__main__':
	device1 = 'speaker'
	device2 = 'headphone'
	unmuteSystemSoundsExe = os.path.join(os.path.dirname(__file__), r'..\UnmuteSystemSounds\UnmuteSystemSounds.exe')
	soundVolumeViewExe = os.path.join(os.path.dirname(__file__), r'..\SoundVolumeView\soundvolumeview-x64\SoundVolumeView.exe')
	subprocess.run(unmuteSystemSoundsExe)
	subprocess.run(f'{soundVolumeViewExe} /switchdefault {device1} {device2} all')
	winsound.MessageBeep(-1)
