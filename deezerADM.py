import time
import subprocess

while True:
	logs = subprocess.run(['tail', '-n', '12', 'logs.txt'], stdout=subprocess.PIPE)
	if logs.stdout.decode('utf-8')[7:19] == 'nuvolaplayer':
		subprocess.run(['pacmd', 'set-sink-input-mute', '127', 'true'])
	else:
		subprocess.run(['pacmd', 'set-sink-input-mute', '127', 'false'])
#	print('\r', logs.stdout.decode('utf-8')[7:19], end='')
