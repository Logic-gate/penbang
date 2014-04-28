#!/usr/bin/env python

# Penbang Install (penbang_install.py)
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

# Report any issues with this script to <mad_dev[at]linuxmail[dot]org>
#								     OR <ammer.almadani[at]sysbase.org[dot]org>

# Tested on crunchbang waldorf(openbox)

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
        self.YEL = ''
        self.RED = ''
        self.ENDC = ''
        self.MOV = ''

dictTools = ['wpscan', 'w3af', 'tor', 'patator', 'climber',
				 'xplico', 'mantra', 'ZAP', '0.5_update']

	#Since the migration to a repo, we need to make sure that the transaction stays smooth.
	#dictTools will contain the latest tools
	#dictTools_%i will contain tools from %i version

dictTools_2 = ['aircrack-ng', 'armitage', 'ettercap',
				   'findmyhash', 'hydra', 'kismet', 'metasploit',
					'nessus', 'openvas', 'SMITM', 'sqlninja',
					'sqlsus', 'subterfuge', 'wfuzz', 'yamas', 'maltego']

dictTools_3 = ['argus', 'arping', 'callerpy', 'fragroute', 
					'nikto', 'ntop', 'ophcrack', 'slowloris',
					'snort', 'spike', 'sqlmap']

def pychk(name, searchLink, searchCommand, search):
	try:
		return __import__(name)
		import name
	except ImportError, e:
		if searchLink != ' ':
			print clr.RED + '#' * 10 + 'NOTICE' + '#' *10 + clr.ENDC
			print clr.MOV + name + clr.YEL + ' module does not exist\nFind our more here: ' + clr.MOV + searchLink + clr.ENDC
		else:
			print clr.MOV + 'Could Note Import Module %s ' %name
			print clr.YEL + 'Search For Module: https://duckduckgo.com/?q=%s' %search
			print clr.ENDC
		if searchCommand != ' ':
			print clr.YEL
			x = raw_input("Shall I search Your Distro's Rep for %s? Y/N " %name)
			print clr.HEADER
			if x == 'y':
				os.system('sudo apt-cache search %s | grep -i python' %searchCommand)
			elif x == 'n':
				print clr.MOV
				print 'Command = %s' %searchCommand
		print clr.ENDC
		sys.exit(0)


import os 
pychk('urllib2', 'http://docs.python.org/2/library/urllib2.html', 'urllib2', 'urllib2')
import urllib2
pychk('subprocess', 'http://docs.python.org/2/library/subprocess.html', ' ', 'subprocess')
import subprocess
pychk('threading', 'http://docs.python.org/2/library/threading.html', ' ', 'threading')
import threading
pychk('sys', ' ', ' ', 'sys') #not needed, unless python is running on a banana
import sys 
pychk('time', ' ', ' ', 'time')
import time
pychk('datetime', ' ', ' ', 'datetime')
import datetime
pychk('itertools', 'http://www.python.org/doc//current/library/itertools.html', ' ', 'itertools')
import itertools
pychk('getpass', 'http://docs.python.org/2/library/getpass.html', ' ', 'getpass')
import getpass      

def check(version): # version stands for the previous version
	path = os.path.abspath('') + '/'  #Check Path
	whoami = getpass.getuser()
	corPath = '/home/%s/penbang/' %whoami
	if path == corPath:
		readme= open('netkit/netkit_source/Scripts.py', 'r')
		a = readme.read()
		version_string = "version = '%s'" %version
		if version_string in  a:
			print clr.OKGREEN
			print 'VERSION STATUS:'
			print clr.YEL
			print 'Based on your Scripts.py script. ' + version_string
			print clr.OKGREEN
			print 'CHECKING UPDATE DEPENDENCIES'
			dep_list = ['dos2unix', 'build-essential', 'gcc', 'aircrack-ng', 'armitage', 'ettercap',
				   'findmyhash', 'hydra', 'kismet', 'metasploit',
					'nessus', 'openvas', 'SMITM', 'sqlninja',
					'sqlsus', 'subterfuge', 'wfuzz', 'yamas', 'maltego']
			"""Other DEPENDENCIES will be downloaded according to install_tool"""
			for dep in dep_list:
				print clr.MOV
				print 'Checking for %s' %dep
				print clr.YEL
				b = os.system('sudo find /var/lib/dpkg/info/'+dep+'.list;') #assuming DL from manager 
				if b:
					print clr.YEL
					print 'I need to download %s' %dep
					print clr.ENDC
					pro = raw_input('Shall I Proceed? y/n ')
					if pro == 'y':
						os.system('sudo apt-get install ' + dep)
						print clr.ENDC
					else:
						print 'Cannot proceed with update without %s....quiting' %dep
						sys.exit(0)
				else:
					print clr.YEL
					print 'Found it'
					print clr.ENDC
		else:
			print clr.RED
			print 'This update assumes version %s is already installed' %version
			print clr.YEL
			print 'http://penbang.sysbase.org/scripts/'+version+'/penbang_'+version+'_update.py'
			print clr.ENDC
	else:
		print clr.RED
		print 'Wrong Path ' + clr.MOV + str(path)
		print clr.YEL
		print 'The Correct Path Must Be '+  clr.MOV +corPath
		print clr.ENDC


def prep(): 
	#Download and install the 'install_tool.sh' scripts from install_tools/
	#Read http://sourceforge.net/p/penbang/wiki/General%20How-To/ for adding a new install scripts 
	up_version = '0.5/' #Do not forget /
	server = 'http://penbang.sysbase.org/install_tools/%s' %up_version
	for tool in dictTools:
		print clr.OKGREEN
		install_tool = 'install_%s.sh' %tool
		filePath = 'netkit/%s' %tool
		print 'Downloading %s to %s' %(install_tool, filePath)
		print clr.ENDC
		if not os.path.exists(filePath): os.makedirs(filePath)
		dl_command = 'wget -P %s %s%s' %(filePath,server,install_tool)
		#print dl_command
		dl = os.system(dl_command)
		print clr.OKGREEN
		name = raw_input('Do you want me to install %s? Y/N ' %tool)
		print clr.YEL
		if name == 'y':
			os.system("dos2unix "+filePath+'/'+install_tool) #To remove ^M
			os.system('chmod +x /home/$(whoami)/penbang/'+filePath+'/'+install_tool)
			os.system('cd /home/$(whoami)/penbang/'+filePath+ ' && ./'+install_tool)
		elif name == 'n':
			print clr.RED
			print 'pass'
			print clr.ENDC
			pass
		else:
			print clr.RED
			print 'Wrong input...Pass'
			print clr.ENDC
			pass

def kernelStuff():
	# Should Consider Adding SELinux!!!
	dictlist = ['linux-patch-grsecurity2']
	for pkg in dictlist:
		while 1:
			x = raw_input('Shall I proceed with installing %s? y/n ' %pkg)
			if x == 'y':
				print 'Installing ' + clr.YEL + pkg + clr.ENDC
				os.system('sudo apt-get install '+ pkg)
				pass
				sys.exit(0)
			elif x == 'n':
				print clr.YEL + 'Fine By me...' + clr.ENDC
				pass
				sys.exit(0)
			else:
				print 'y/n'

if __name__ == "__main__":

	if len(sys.argv) > 1: updateFunc=sys.argv[1]
	if updateFunc == '-check':
		check('0.0.3') #check if the previous version is installed
	if updateFunc == '-update':
		print '\nVERSION 0.5 Update'
		prep()
		print '\nChanging Name in menu.xml'
		whoami = getpass.getuser()
		o = open("/home/"+whoami+"/.config/openbox/menu.xml","w")
		for line in open("/home/"+whoami+"/penbang/mod_data/openbox/menu.xml"):
			line = line.replace("mad-dev",str(whoami)) #Change the name so that the Icons appear
			o.write(line)
			print 'done'
		o.close()
	if updateFunc == '-kernel':
		kernelStuff()