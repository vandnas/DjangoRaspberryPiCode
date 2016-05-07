import shutil
import time
import os


PINUT_JSON_FILEPATH="/home/pi/PinutJsonFiles"
TEMP_UPLOAD_PINUT_JSON_FILEPATH="/home/pi/UploadDir/PinutJsonFiles_temp"

def get_pinut_device_timestamp():
        #Check if local Or UTC needs to be sent ??
        return time.time()


def get_params_from_pinutuser_file(filename):
        try:
                split_name=filename.split("_")
                pinut_mac_var=split_name[1]
                pinut_mac = ':'.join(pinut_mac_var[i:i+2] for i in range(0, len(pinut_mac_var), 2))
                day=split_name[2]
                month=split_name[3]
                year=split_name[4].split(".")[0]
                date_in_filename=str(day)+"-"+str(month)+"-"+str(year)
                return date_in_filename
        except Exception, e:
                logging.exception("Exception [%s] in getting params for filename[%s] ", e, filename)
                raise


def mkgmtime(x):
    ltime_sec = time.mktime(x)
    ltime = time.localtime(ltime_sec)
    if ltime.tm_isdst and time.daylight:
        ret_time = ltime_sec - time.altzone
    else:
        ret_time = ltime_sec - time.timezone
    return ret_time


def convert_date_str_to_timestamp(date_str):
    return (mkgmtime(time.strptime(date_str, '%d-%m-%Y')))

def create_directory(path):
        try:
                if not os.path.exists(path):
                        os.makedirs(path)
			#os.chmod(path, mode)
        except Exception,e:
                print "Exception : %s Not able to create directory : %s" % (e,path)


def send_old_json_files_to_upload_dir(TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP):
	try:
		#Send current_date -1 files to AWS
		if os.path.exists(PINUT_JSON_FILEPATH):
			for dir in os.listdir(PINUT_JSON_FILEPATH):
				DIR_PATH=PINUT_JSON_FILEPATH + "/" + str(dir)
				for filename in os.listdir(DIR_PATH):
					FILE_PATH=DIR_PATH + "/" + str(filename)
					date_in_filename = get_params_from_pinutuser_file(FILE_PATH)
					file_timestamp = convert_date_str_to_timestamp(date_in_filename)
					current_timestamp = get_pinut_device_timestamp()
					oneday = 60*60*24 # Number of seconds in one day
					if (current_timestamp - file_timestamp) > oneday:
						#shutil.move(FILE_PATH , TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP)
						print "Copying file :",FILE_PATH, "to :",TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP
						shutil.copy2(FILE_PATH , TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP)

		#Create zip folder
                shutil.make_archive(TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP, 'zip', TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP)
                shutil.rmtree(TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP, ignore_errors=True)

	except Exception, e:
		print "Error in sending old json files to upload dir", e
		raise


def send_files_to_upload_dir():
	try:
		current_timestamp = get_pinut_device_timestamp()
                TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP=TEMP_UPLOAD_PINUT_JSON_FILEPATH + "_" + str(current_timestamp)
                create_directory(TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP)
		send_old_json_files_to_upload_dir(TEMP_UPLOAD_PINUT_JSON_FILEPATH_WITH_TIMESTAMP)
	except Exception, e:
		print "Error in uploading folder to aws", e
		raise
				
				
if __name__ == '__main__':
	send_files_to_upload_dir()	
			
			
		

