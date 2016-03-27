from django.conf import settings
import os

PINUT_PATH="/home/vandna/pinut"
PINUT_USER_INTRO_FILE_PATH = PATH + "/" + "PinutUserIntroFiles"
PINUT_USER_FILE_PATH = PATH + "/" + "PinutUserFiles"
PINUT_CONNECTION_FILE_PATH = PATH + "/" + "PinutConnectionFiles"

def get_pinut_mac_address():
        # Return the MAC address of interface
        try:
                str = open('/sys/class/net/eth0/address').read()
        except:
                str = "00:00:00:00:00:00"
        return str[0:17]

def create_directory(path):
	try:
		if not os.path.exists(path):
			os.makedirs(path)
	except Exception,e:
		print "Exception : %s Not able to create directory : %s" % (e,path)


PINUT_MAC = get_pinut_mac_address()
create_directory(PINUT_USER_INTRO_FILE_PATH)
create_directory(PINUT_USER_FILE_PATH)
create_directory(PINUT_CONNECTION_FILE_PATH)

