#!/usr/bin/env python

# Penbang Installer (install.py)
# Copyright (C) <2013>  mad_dev(A'mmer Almadani)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Report any issues with this script to <mad_dev@linuxmail.org>

# Tested on crunchbang waldorf(openbox)

# 3rd party DISCLAIMER
#
# pingCommunication Class {
# 	Description: This module tests a ping return
# 	Author: Thiago de Freitas Oliveira Araujo
# 
# 	<http://thiagodefreitas.com>
# 
# 	<thiago@thiagodefreitas.com> }
#
# EODISCLAIMER


# This entire script must be rewritten

def pychk(name, downloadFile, downloadCommand, search):
	try:
		return __import__(name)
		import name
	except ImportError, e:
		if downloadFile != ' ':
			print name + ' does not exist\nFind our more here: ' + downloadFile
		else:
			print '%s usually comes with python' %name
			print 'Link: https://duckduckgo.com/?q=%s' %search
		if downloadCommand != ' ':
			x = raw_input("Download %s? Y/N " %name)
			if x == 'y':
				os.system(downloadCommand)
			elif x == 'n':
				print 'Command %s' %downloadCommand
		a = input('Hit enter to exit')

import os 
pychk('urllib2', ' ', ' ', 'urllib2')
import urllib2
pychk('subprocess', ' ', ' ', 'subprocess')
import subprocess
pychk('threading', ' ', ' ', 'threading')
import threading
pychk('sys', ' ', ' ', 'sys') #not needed, unless python is running on a banana
import sys 
pychk('time', ' ', ' ', 'time')
import time
pychk('datetime', ' ', ' ', 'datetime')
import datetime
pychk('itertools', ' ', ' ', 'itertools')
import itertools
pychk('getpass', ' ', ' ', 'getpass')
import getpass

version="0.0.2"

class clr:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    YEL = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    MOV = '\033[96m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''
        self.MOV = ''


class pingCommunication():

   	def __init__(self, ipToPing):
        	self.ipToPing = ipToPing
        	self.pingQuantity = "5" #seems enough

	def pingProcess(self):
        	pingTest = "ping -c "+ self.pingQuantity + ' ' + self.ipToPing
        	print "Checking if you are connected by " + pingTest
        	process = subprocess.Popen(pingTest, shell=True, stdout=subprocess.PIPE)
        	process.wait()
        	returnCodeTotal = process.returncode
		while 1:
        		if returnCodeTotal < 1:
				pass
				time.sleep(0.1)
				print "\nConnection Test Passed\n"
				time.sleep(0.1)
				print 'Penbang %s\n' %version
				print clr.HEADER
				print '''To install yamas, cd to its dir and run it from the root terminal.
Dont run sudo yamas, run sudo su, then yamas.\n'''
				print clr.ENDC
				print clr.OKGREEN
				awoken = raw_input('Do you want me to download AwOken Icons? Y/N ')
				print clr.YEL
				if awoken == 'y':
					os.system('wget -P /home/$(whoami)/penbang/awoken_icons/zip https://dl.dropbox.com/u/8029324/AwOken-2.5.zip')
					os.system('unzip -n /home/$(whoami)/penbang/awoken_icons/zip/AwOken-2.5.zip -d /home/$(whoami)/penbang/awoken_icons/zip/')
					os.system('tar -xvf /home/$(whoami)/penbang/awoken_icons/zip/AwOken-2.5/AwOken.tar.gz -C /home/$(whoami)/penbang/awoken_icons/zip/AwOken-2.5/')
					os.system('mv /home/$(whoami)/penbang/awoken_icons/zip/AwOken-2.5/AwOken /home/$(whoami)/.icons/')
				elif awoken == 'n':
					print 'pass'
					pass
				else:
					print 'Wrong input'
					awoken
				print clr.HEADER
				print '''Initial installation:\033[93m
terminator \033[94m#Just in case\033[93m 
irpas
dsniff
nmap
wireshark
tshark
zenmap
sslstrip
sslsniff
reaver
tcpdump
scapy
john
gdebi \033[94m#Just in case'''
				print clr.OKGREEN
				root=raw_input('Shall I proceed with the initial installation? Y/N ')
				print clr.YEL
				if root == 'y':
					os.system('sudo apt-get update')
					os.system('sudo apt-get install terminator') #Everything will be launched using terminator
					os.system('sudo apt-get install irpas')
					os.system('sudo apt-get install dsniff')
					os.system('sudo apt-get install nmap')
					os.system('sudo apt-get install wireshark')
					os.system('sudo apt-get install tshark')
					os.system('sudo apt-get install zenmap')
					os.system('sudo apt-get install sslstrip')
					os.system('sudo apt-get install sslsniff')
					os.system('sudo apt-get install reaver')
					os.system('sudo apt-get install tcpdump')
					os.system('sudo apt-get install scapy')
					os.system('sudo apt-get install john')
					os.system('sudo apt-get install gdebi') #Needed for .deb
				elif root == 'n':
					print 'Passing inital'
					pass
				break
		else:
			print clr.RED
			print "You are not connected to the Internet"
			print "Killing process...Bye"
			raise SystemError("Failed to connect")


if __name__ == "__main__":
	print clr.RED
	print 'DO NOT RUN THIS AS ROOT\nASSUMES AN i386 SYSTEM'
	print clr.OKBLUE
	print 'You will be prompted at several points to enter your root password.\n'
	print clr.ENDC
	#Ipadd = "173.194.40.17" #Google.com
	Ipadd = "72.14.179.38" #Crunchbang.com
   	comunicate = pingCommunication(Ipadd)
   	comunicate.pingProcess()
   	os.system('exit') #WHY???????
   	print clr.RED
   	#print 'This version includes openvas 6.\nThere have been some reports that\n\033[93mGreenbone Security Desktop (GSD) 1.2.2\n\033[91mDoes not build on newer systems\nPlease read the *) note on\n\033[93mhttp://www.openvas.org/install-source.html'
	
	print clr.ENDC
	print "I need to change menu.xml\nDon't worry. Your old config will be renamed menu_orig.xml?"
	print clr.OKGREEN
   	openbox = raw_input("Shall I change menu.xml Y/N ")
   	if openbox == 'y':
		print clr.YEL
   		os.system('cp /home/$(whoami)/.config/openbox/menu.xml /home/$(whoami)/.config/openbox/menu_orig.xml')
   		#os.system('cp /home/$(whoami)/penbang/mod_data/openbox/menu.xml /home/$(whoami)/.config/openbox/menu.xml')
   		##################Needed for icons in menu###############################
   		whoami = getpass.getuser()
		o = open("/home/"+whoami+"/.config/openbox/menu.xml","w")
		for line in open("/home/"+whoami+"/penbang/mod_data/openbox/menu.xml"):
			line = line.replace("mad-dev",str(whoami))
			o.write(line)
		o.close()
		########################################################################
   	elif openbox == 'n':
		print clr.RED
   		print 'pass'
   		pass
   	else:
		print clr.RED
   		print 'Wrong input..wrong'
   		pass
   	
   	def install_tool(name, path):
		print clr.OKGREEN
		name = raw_input('Do you want me to install %s? Y/N ' %name)
		print clr.YEL
		if name == 'y':
			os.system(path)
		elif name == 'n':
			print clr.RED
			print 'pass'
			pass
		else:
			print clr.RED
			print 'Wrong input...Pass'
			pass
			
   	install_tool('maltego', '/home/$(whoami)/penbang/social_engineering/maltego_community/install_maltego.sh')
	install_tool('aitcrack-ng', '/home/$(whoami)/penbang/netkit/aircrack-ng/source/install_aircrack.sh')
	install_tool('ettercap', '/home/$(whoami)/penbang/netkit/ettercap/install_ettercap.sh')
	install_tool('kismet', '/home/$(whoami)/penbang/netkit/kismet/install_kismet.sh')
	install_tool('metasploit', '/home/$(whoami)/penbang/netkit/metasploit/install_metasploit.sh')
	install_tool('armitage', '/home/$(whoami)/penbang/netkit/armitage/install_armitage.sh')
	install_tool('sqlninja', '/home/$(whoami)/penbang/netkit/sqlninja/install_sqlninja.sh')
	#install_tool('nessus', 'home/$(whoami)/penbang/netkit/nessus/install_nessus.sh')
	#install_tool('openvas', '/home/$(whoami)/penbang/netkit/openvas/install_openvas.sh') #Facing some build issues, I will include it in the next release
	install_tool('sqlsus', '/home/$(whoami)/penbang/netkit/sqlsus/install_sqlsus.sh')
	install_tool('wfuzz', '/home/$(whoami)/penbang/netkit/wfuzz/install_wfuzz.sh')
	install_tool('hydra', '/home/$(whoami)/penbang/netkit/hydra/install_hydra.sh')
	install_tool('findmyhash', '/home/$(whoami)/penbang/netkit/findmyhash/install_findmyhash.sh')
	install_tool('SMITM', '/home/$(whoami)/penbang/netkit/SMITM/install_smitm.sh')
	install_tool('subterfuge', '/home/$(whoami)/penbang/netkit/subterfuge/install_subterfuge.sh')



