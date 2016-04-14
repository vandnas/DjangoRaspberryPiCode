import subprocess

upload_list = ["/home/vandna/Desktop/test_folder","/home/vandna/Desktop/test_folder1"]
#TODO: Keep public keys on raspberry pi and change below path
keys = "/home/vandna/pinut/pinut_wordpress_keypair.pem"
dest_username = "ec2-user"
dest_hostname = "ec2-54-169-232-88.ap-southeast-1.compute.amazonaws.com"
dest_path = "/home/ec2-user"
remote_host = "ec2-user@ec2-54-169-232-88.ap-southeast-1.compute.amazonaws.com"

for upload_folder in upload_list:
	dest_cmd = "%s@%s:%s" % (dest_username, dest_hostname, dest_path)
	pipe = subprocess.Popen(['scp', '-i', keys, '-r', upload_folder, dest_cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = pipe.communicate()
	print "out",out
	print "err",err
	if err is not "":
		print "Error :%s in uploading folder : %s to cloud" % (err, upload_folder)



#scp -i "/home/vandna/pinut/pinut_wordpress_keypair.pem" -r /home/vandna/Desktop/test_folder ec2-user@ec2-54-169-232-88.ap-southeast-1.compute.amazonaws.com:/home/ec2-user/

