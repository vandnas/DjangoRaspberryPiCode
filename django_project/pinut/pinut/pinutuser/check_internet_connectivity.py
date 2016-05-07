import requests
import gzip
import json
import os
import urllib2


TEMP_UPLOAD_PINUT_JSON_FILEPATH="/home/pi/UploadDir"
AWS_URL = "http://54.169.232.88:8000/pinutcloud/uploadjsonfiles/"
USERNAME="admin"
PASSWORD="admin"


def test_internet_connection():
	loop_value = True
	ic_flag=0
	while loop_value:
		try:
			print "IN TRY"
			urllib2.urlopen("http://google.com")
		except urllib2.URLError, e:
			print "IN EXCEPT"
			print "Network currently down."
		else:
			print( "Up and running." )
			#The code to upload a file to my server goes here
			loop_value = 0
			ic_flag=1
	return ic_flag
	

def upload_folder_to_aws():
	try:
		ic_flag=test_internet_connection
		if ic_flag:
			for folder in os.listdir(TEMP_UPLOAD_PINUT_JSON_FILEPATH):
				with open(TEMP_UPLOAD_PINUT_JSON_FILEPATH+"/"+folder, 'r') as content_file:
					content = content_file.read()
				print "content",content
				#r = requests.post(AWS_URL, content, auth=(USERNAME, PASSWORD))
				r = requests.post(AWS_URL, content)
				print "r.info", r.status_code
	except Exception, e:
		print "Error in uploading folder to aws", e
		raise
				
				
if __name__ == '__main__':
	upload_folder_to_aws()	
			
			
		

