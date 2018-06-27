#Author: Ifan Mohammed
#27/06/2018

import urllib

def getUrl():
	url = "http://www.google.com"	#raw_input("  Enter the URL: ")
        url=url.rstrip()
        headers_reader(url)

def headers_reader(url):

	print (" \n  Getting the Server information ....")
	opener = urllib.urlopen(url) #reads the whole webpage content
	if opener.code == 200:
		 print  "Status code: 200 OK \n"
	if opener.code == 404:
		 print " Page was not found! Please check the URL \n"
		 exit()
	Server = opener.info() #reads the HTTP headers
	Host = url.split("/")[2]
	print "Host: " + str(Host) + "\n"
	print "Headers:\n\n " + str(Server)

getUrl()
