#!/usr/bin/python

import requests
import os
import urllib2
import datetime


TEMP_UPLOAD_PINUT_JSON_FILEPATH="/home/pi/UploadDir"
AWS_URL = "http://54.169.232.88:8080/pinutcloud/uploadjsonfiles/"
#USERNAME="admin"
#PASSWORD="admin"


def test_internet_connection():
	loop_value = True
	ic_flag=0
	while loop_value:
		try:
			urllib2.urlopen("http://google.com")
		except urllib2.URLError, e:
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
				#r = requests.post(AWS_URL, content, auth=(USERNAME, PASSWORD))
				r = requests.post(AWS_URL, content)
				httpd_code = r.status_code
				if httpd_code == 200:
					print ("%s: Json File Upload Successful to AWS : %s" % (datetime.datetime.utcnow(), folder))
					os.remove(TEMP_UPLOAD_PINUT_JSON_FILEPATH+"/"+folder)
				else:
					print ("%s: Unable to upload Json File to AWS : %s .. Will try next time" % (datetime.datetime.utcnow(), folder))
				
	except Exception, e:
		print ("Error in uploading folder to aws : %s" % e)
		raise
				
				
if __name__ == '__main__':
	try:
		if os.listdir(TEMP_UPLOAD_PINUT_JSON_FILEPATH) != []:
			upload_folder_to_aws()	
	except Exception, e:
		print ("Exception %s" % e)
			
			
		

