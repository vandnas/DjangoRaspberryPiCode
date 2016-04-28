# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.http import HttpResponse
import time
import json
import os
from pinutuser import PINUT_MAC, PINUT_USER_INTRO_FILE_PATH, PINUT_USER_FILE_PATH, PINUT_CONNECTION_FILE_PATH, PINUT_FEEDBACK_FILE_PATH

def get_pinut_device_timestamp():
	#The time.time() function returns the number of seconds since the epoch as seconds in UTC.
	return int(time.time())

def get_pinut_device_date():
	#Check if local Or UTC needs to be sent ??(cron job -local , filenames , in mongo , in postgres)
	return time.strftime("%d_%m_%Y")

def remove_colons_from_mac(mac):
	mac_list=mac.split(':')
	MAC = ''.join([str(mac) for mac in mac_list])
	return MAC

PINUT_MAC = remove_colons_from_mac(PINUT_MAC)
today_date = get_pinut_device_date()

#PINUT USER INTRO FILE
#Dump these record into json files PinutUserIntro_d1f5c60cb9ff_18_01_2016.json
#{"cl_mac":"c1:f5:c6:0c:b9:ef","phone":8000678800,"email_id":"c1@gmail.com", "name":priya}
PINUT_USER_INTRO_FILE_NAME="PinutUserIntro"
PINUT_USER_INTRO_JSON_FILE=str(PINUT_USER_INTRO_FILE_PATH)+"/"+str(PINUT_USER_INTRO_FILE_NAME)+"_"+(PINUT_MAC)+"_"+str(today_date)+".json"


#PINUT USER FILE
#Dump these record into json files PinutUser_d1f5c60cb9ff_18_01_2016.json
#{"cl_mac":"c1:f5:c6:0c:b9:ef","phone":8000678800,"email_id":"c1@gmail.com","data":"bajrangi bhaijan.mp4","category":"movie","device_timestamp":14508461}
PINUT_USER_FILE_NAME="PinutUser"
PINUT_USER_JSON_FILE=str(PINUT_USER_FILE_PATH)+"/"+str(PINUT_USER_FILE_NAME)+"_"+(PINUT_MAC)+"_"+str(today_date)+".json"

#PINUT CONNECTION FILE
#{c1:f5:c6:0c:b9:ef:{"connection":1}}
PINUT_CONNECTION_FILE_NAME="PinutConnection"
PINUT_CONNECTION_JSON_FILE=str(PINUT_CONNECTION_FILE_PATH)+"/"+str(PINUT_CONNECTION_FILE_NAME)+"_"+(PINUT_MAC)+"_"+str(today_date)+".json"


#PINUT FEEDBACK FILE
#{ "cl_mac":"c7:f5:c6:0c:b9:ef", "phone":”8000678800”, "email_id":"c1@gmail.com", "name":"priya", "ride_experience":3, "pinut_experience":5, “comment”:”Love the new entertainment media”}
PINUT_FEEDBACK_FILE_NAME="PinutFeedback"
PINUT_FEEDBACK_JSON_FILE=str(PINUT_FEEDBACK_FILE_PATH)+"/"+str(PINUT_FEEDBACK_FILE_NAME)+"_"+(PINUT_MAC)+"_"+str(today_date)+".json"
#TODO:Zip json files

def byteify(input):
   if isinstance(input, dict):
       return {byteify(key):byteify(value) for key,value in input.iteritems()}
   elif isinstance(input, list):
       return [byteify(element) for element in input]
   elif isinstance(input, unicode):
       return input.encode('utf-8')
   else:
       return input



#Dump into User Json Files
#POST REQUEST
def userintro(request):
	print "Inside user intro file" , PINUT_MAC
	if request.method == "POST":
		print "Inside POST request"
		pinut_user_intro_dict={}
		#Get body from post request
		msg=request.body;
		print "msg",msg
		#Decode it
		string_msg=msg.decode("utf-8")
		print "string_msg",string_msg
		#Load into Json format
		json_data=json.loads(string_msg);
		print "json_data",json_data
		#Byteify it
		pinut_user_intro_dict=byteify(json_data)
		with open(PINUT_USER_INTRO_JSON_FILE, 'a') as fp:
			json.dump(pinut_user_intro_dict, fp)
			fp.write('\n')
		
		return HttpResponse("You're in POST request.")
	else:
		print "Its a GET request"
		return HttpResponse("You're in GET request.")


#Dump into User Json Files
#POST REQUEST
def userinfo(request):

	if request.method == "POST":
		pinut_user_dict={}
		#Get body from post request
		msg=request.body;
		#Decode it
		string_msg=msg.decode("utf-8")
		#Load into Json format
		json_data=json.loads(string_msg);
		#Byteify it
		pinut_user_dict=byteify(json_data)
		pinut_user_dict['device_timestamp']=get_pinut_device_timestamp()
		with open(PINUT_USER_JSON_FILE, 'a') as fp:
			json.dump(pinut_user_dict, fp)
			fp.write('\n')
		
		return HttpResponse("You're in POST request.")
	else:
		print "Its a GET request"
		return HttpResponse("You're in GET request.")

#Dump into COnnection Json Files
#POST REQUEST
def connectioninfo(request):
	if request.method == "POST":
		connection_dict={}
		pinut_connection_dict={}
		#Get body from post request
		msg=request.body;
		#Decode it
		string_msg=msg.decode("utf-8")
		#Load into Json format
		json_data=json.loads(string_msg);
		#Byteify it
		connection_dict=byteify(json_data)
		cl_mac=connection_dict['cl_mac']
		#If file already exist
		if os.path.exists(PINUT_CONNECTION_JSON_FILE):
			with open(PINUT_CONNECTION_JSON_FILE, 'r') as data_file:
				#Load entire file to dictionary
				pinut_connection_dict = json.load(data_file)
				#Check if clmac exist in that dictionary.If yes, increment its connection counter else set it to 1.
				if str(cl_mac) in pinut_connection_dict.keys():
					counter=pinut_connection_dict[str(cl_mac)]
					count=counter['connection']
					counter['connection']=count+1
				else:
					counter={}
					counter['connection']=1
				
		else:
			#Create file for the first time
			counter={}
			counter['connection']=1

		#Dump the dictionary back into the file.
		pinut_connection_dict[str(cl_mac)]=counter
		with open(PINUT_CONNECTION_JSON_FILE, 'w') as fp:
			json.dump(pinut_connection_dict, fp)

		return HttpResponse("You're in POST request.")
	else:
		print "Its a GET request"
		return HttpResponse("You're in GET request.")
		
		
#Dump into Feedback Json Files
#POST REQUEST
def feedback(request):

	if request.method == "POST":
		pinut_feedback_dict={}
		#Get body from post request
		msg=request.body;
		#Decode it
		string_msg=msg.decode("utf-8")
		#Load into Json format
		json_data=json.loads(string_msg)
		#Byteify it
		pinut_feedback_dict=byteify(json_data)
		with open(PINUT_FEEDBACK_JSON_FILE, 'a') as fp:
			json.dump(pinut_feedback_dict, fp)
			fp.write('\n')
		
		return HttpResponse("You're in POST request.")
	else:
		print "Its a GET request"
		return HttpResponse("You're in GET request.")
