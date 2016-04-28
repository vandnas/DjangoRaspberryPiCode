import urllib2

loop_value = True
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
