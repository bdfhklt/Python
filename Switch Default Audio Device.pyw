import os, subprocess, winsound, configparser

if __name__ == '__main__':
	device1 = 'Speaker'
	device2 = 'Headphone'
	unmuteSystemSoundsExe = os.path.join(os.path.dirname(__file__), r'..\UnmuteSystemSounds\Release\net5.0\UnmuteSystemSounds.exe')
	soundVolumeViewExe = os.path.join(os.path.dirname(__file__), r'..\SoundVolumeView\soundvolumeview-x64\SoundVolumeView.exe')
	subprocess.run(unmuteSystemSoundsExe)

	configFile = os.path.splitext(__file__)[0] + '.ini'
	config = configparser.ConfigParser()
	config.read(configFile)
	def setDefaultAudioDevice(deviceName):
		subprocess.run(f'{soundVolumeViewExe} /SetDefault {deviceName} all')
		config['data'] = {'default audio device': deviceName}
	if config.has_option('data', 'default audio device'):
		if config['data']['default audio device'] == device1:
			setDefaultAudioDevice(device2)
		elif config['data']['default audio device'] == device2:
			setDefaultAudioDevice(device1)
	else:
		setDefaultAudioDevice(device1)
	
	with open(configFile, 'w') as f:
		config.write(f)
	winsound.MessageBeep(-1)
