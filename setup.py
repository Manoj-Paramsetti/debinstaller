import os

# Color
def _success(text):
    print('\033[1;35m'+text+'\033[0m')

if __name__ == '__main__':

	if (os.path.isfile('bin/debinstalle')): 
		pass
		#os.system('cp -r bin/debinstaller /usr/bin/debinstaller')
	else:
		pass
	#	os.system('wget https://raw.githubusercontent.com/Manoj-Paramsetti/debinstaller/main/bin/debinstaller -P /usr/bin/')
	#os.system('chmod +x /usr/bin/debinstaller')

	_success('debinstaller is installed')
