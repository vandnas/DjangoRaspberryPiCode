from django.conf import settings
import os

PATH="/home/pi"
PINUT_JSON_FILE_DIR = PATH + "/" + "PinutJsonFiles"
PINUT_USER_INTRO_FILE_PATH = PINUT_JSON_FILE_DIR + "/" + "PinutUserIntroFiles"
PINUT_USER_FILE_PATH = PINUT_JSON_FILE_DIR + "/" + "PinutUserFiles"
PINUT_CONNECTION_FILE_PATH = PINUT_JSON_FILE_DIR + "/" + "PinutConnectionFiles"
PINUT_FEEDBACK_FILE_PATH = PINUT_JSON_FILE_DIR + "/" + "PinutFeedbackFiles"

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
create_directory(PINUT_JSON_FILE_DIR)
create_directory(PINUT_USER_INTRO_FILE_PATH)
create_directory(PINUT_USER_FILE_PATH)
create_directory(PINUT_CONNECTION_FILE_PATH)
create_directory(PINUT_FEEDBACK_FILE_PATH)

