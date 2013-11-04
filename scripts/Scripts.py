#!/usr/bin/env python

# Scripts.py--Generic launcher for Pen Tools
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
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Report any issues with this script to <mad_dev@linuxmail.org>

# Tested on crunchbang waldorf(openbox)

# 3rd party DISCLAIMER
#
#  *(
#   By pyfunc http://stackoverflow.com/users/432745/pyfunc
#   Posted on http://stackoverflow.com/questions/4289937/how-to-repeat-last-command-in-python-interpreter-shell
#   )*
# EODISCLAIMER

import os
import sys
import bigfig
import readline 
import rlcompleter 
import atexit
import getpass
import signal

#*( 
readline.parse_and_bind('tab: complete') 
histfile = os.path.join(os.environ['HOME'], '.pythonhistory') 
try: 
    readline.read_history_file(histfile) 
except IOError: 
    pass 

atexit.register(readline.write_history_file, histfile) 

del histfile, readline, rlcompleter
#)*

version = '0.5'
def crunchRun():
    print """
 __               
/   __   __  _ |_ 
\__ | |_|| |(_ | |

"""
    while 1:
        x = raw_input("View Examples. Y, N? ")
        if x == 'y':
            os.system("cat /home/$(whoami)/penbang/netkit/netkit_source/crunch-3.4/crunch.expl | less")
            print "\n"
        if x == 'n':
            whoami = getpass.getuser()
            print "Format:\ncrunch [Crunch Command] -o [Outfile Name]\n"
            print "You will be prompted to enter the Output file...\n"
            cmd = raw_input("Crunch Command: ")
            cmd2 = raw_input("Outfile Name: ")
            path = open("/home/"+whoami+"/penbang/netkit/netkit_source/crunchWordList/"+cmd2, 'w+') 
            crunchCommand = "/home/$(whoami)/penbang/netkit/crunch-3.4/crunch %s -o /home/$(whoami)/penbang/netkit/crunch-3.4/crunchWordList/%s" %(cmd, cmd2)
            x = raw_input("Are you sure you want to run\n %s \n(Y, N): " %crunchCommand)
            print "Results will be in the crunchWordList folder"
            print "The terminal will exit when its finished!!" 
            if x == 'y':
                os.system(crunchCommand)
                path.close()
                
            elif x == 'n':
                print "Removing %s ..." %cmd2
                os.system("rm /home/$(whoami)/penbang/netkit/netkit_source/crunchWordList/%s" %cmd2)


def yamasRun(): #sudo yamas rasies a lot of errors. sudo su, then running yamas works. 
    print '''

\ / _     _  __
 Y |_||V||_|(_ 
 | | || || |__)
157.55.32.52 - - [29/Oct/2013:00:11:10 -0700] "GET /robots.txt HTTP/1.1" 200 58

    '''
    print 'Type yamas to start it\n'
    os.system('sudo su')
    
         
def scriptRun(ascii_text, help_command, command):
    print 'version %s' %version
    print '\n'
   # url = "http://sysbase.org/penbang.sysbase.org/htdocs/penbang_msg_centre/msg"
    #url = "http://www.techuff.com/penbang_msg_center/%s.txt" %command #each command has a msg
   # os.system('echo $(curl --silent -q '+str(url)+ ')')
    print ascii_text
    os.system('sudo %s' %help_command)
    while 1:
        x = raw_input(command+"$ ")
        os.system('sudo '+command+' '+x)

def main():
    if len(sys.argv) > 1: function=sys.argv[1]
    if function =="crunch":
        crunchRun()
    if function =="john":
        scriptRun(ascii_text=bigfig.john_ascii, help_command='john', command='john') # You can use this format
    if function =="cdp":
        scriptRun(bigfig.cdp_ascii, 'cdp', 'cdp') # or this
    if function=="file2cable":
        scriptRun(bigfig.file2cable_ascii, 'file2cable', 'file2cable')
    if function=="igrp":
        scriptRun(bigfig.igrp_ascii, 'igrp', 'igrp')
    if function=="ass":
        scriptRun(bigfig.ass_ascii, 'ass', 'ass')
    if function=="irdp":
        scriptRun(bigfig.irdp_ascii, 'irdp', 'irdp')
    if function=='irdpresponder':
        scriptRun(bigfig.irdpresponder_ascii, 'irdpresponder', 'irdpresponder')
    if function=='itrace':
        scriptRun(bigfig.itrace_ascii, 'itrace -a', 'itrace') # -a in help_command to raise help options
    if function=='tctrace':
        scriptRun(bigfig.tctrace_ascii, 'tctrace -a', 'tctrace')  # -a in help_command to raise help options
    if function=='netenum':
        scriptRun(bigfig.netenum_ascii, 'netenum', 'netenum')
    if function=='protos':
        scriptRun(bigfig.protos_ascii, 'protos -a', 'protos')
    if function=='nmap':
        scriptRun(bigfig.nmap_ascii, 'nmap', 'nmap')
    if function=='hsrp':
        scriptRun(bigfig.hsrp_ascii, 'hsrp', 'hsrp')
    if function=='tcpdump':
        scriptRun(bigfig.tcpdump_ascii, 'tcpdump', 'tcpdump')
    if function=='dfkaa':
        scriptRun(bigfig.dfkaa_ascii, 'dfkaa', 'dfkaa')
    if function=='tshark':
        scriptRun(bigfig.tshark_ascii, 'tshark --help', 'tshark')
    if function=='aircrack-ng':
        scriptRun(bigfig.aircrack_ascii, 'aircrack-ng --help', 'aircrack-ng')
    if function=='reaver':
        scriptRun(bigfig.reaver_ascii, 'reaver --help', 'reaver')
    if function=='airodump-ng':
        scriptRun(bigfig.airodump_ascii, 'airodump-ng --help', 'airodump-ng')
    if function=='airmon-ng':
        scriptRun(bigfig.airmon_ascii, 'airmon-ng --help', 'airmon-ng')
    if function=='sslsniff':
        scriptRun(bigfig.sslsniff_ascii, 'sslsniff', 'sslsniff')
    if function=='sslstrip':
        scriptRun(bigfig.sslstrip_ascii, 'sslstrip --help', 'sslstrip')
    if function=='yamas':
        yamasRun() #sudo yamas rasies a lot of errors. sudo su, then running yamas works. 
    if function=='kismet':
        scriptRun(bigfig.kismet_ascii, 'kismet --help', 'kismet')
    if function=='dsniff':
        scriptRun(bigfig.dsniff_ascii, 'dsniff -help', 'dsniff')
    if function=='filesnarf':
        scriptRun(bigfig.filesnarf_ascii, 'filesnarf -help', 'filesnarf')
    if function=='mailsnarf':
        scriptRun(bigfig.mailsnarf_ascii, 'mailsnarf -help', 'mailsnarf')
    if function=='urlsnarf':
        scriptRun(bigfig.urlsnarf_ascii, 'urlsnarf -help', 'urlsnarf')
    if function=='msgsnarf':
        scriptRun(bigfig.msgsnarf_ascii, 'msgsnarf -help', 'msgsnarf')
    if function=='webspy':
        scriptRun(bigfig.webspy_ascii, 'webspy -help', 'webspy')
    if function=='arpspoof':
        scriptRun(bigfig.arpspoof_ascii, 'arpspoof -help', 'arpspoof')
    if function=='dnsspoof':
        scriptRun(bigfig.dnsspoof_ascii, 'dnsspoof -help', 'dnsspoof')
    if function=='macof':
        scriptRun(bigfig.macof_ascii, 'macof -help', 'macof')
    if function=='sshmitm':
        scriptRun(bigfig.sshmitm_ascii, 'sshmitm -help', 'sshmitm')
    if function=='webmitm':
        scriptRun(bigfig.webmitm_ascii, 'webmitm -help', 'webmitm')
    if function=='subterfuge':
        scriptRun(bigfig.subterfuge_ascii, 'subterfuge -help', 'subterfuge')
    if function=='ettercap':
        scriptRun(bigfig.ettercap_ascii, 'ettercap -help', 'ettercap')
    #if function=='nessus':
    #    scriptRun(bigfig.nessus_ascii, '/etc/init.d/nessusd', '/etc/init.d/nessusd')
    if function=='sqlninja':
        scriptRun(bigfig.sqlninja_ascii, 'sqlninja --help', 'sqlninja')
    if function=='etherape':
        scriptRun(bigfig.etherape_ascii, 'etherape --help', 'etherape')
    if function=='sqlsus':
        scriptRun(bigfig.sqlsus_ascii, 'sqlsus', 'sqlsus')
    if function=='wfuzz':
        scriptRun(bigfig.wfuzz_ascii, 'wfuzz', 'wfuzz')
    if function=='hydra':
        scriptRun(bigfig.hydra_ascii, 'hydra --help', 'hydra')
    if function=='findmyhash':
        scriptRun(bigfig.findmyhash_ascii, 'findmyhash', 'findmyhash')
    if function=='parselog':
        scriptRun(bigfig.parselog_ascii, 'echo', 'parselog') #echo for empty output
    if function=='log_ex':
        scriptRun(' ', 'log_ex --help', 'log_ex')
    if function=='slowloris':
        scriptRun(' ', 'slowloris.pl', 'slowloris.pl') # 0.0.3
    if function=='slowloris6':
        scriptRun(' ', 'slowloris6.pl', 'slowloris6.pl')
    if function=='argus':
        scriptRun(bigfig.argus_ascii, 'argus --help', 'argus')
    if function=='arping':
        scriptRun(bigfig.arping_ascii, 'arping --help', 'arping')
    if function=='ntop':
        scriptRun(bigfig.ntop_ascii, 'ntop --help', 'ntop')
    if function=='fragroute':
        scriptRun(bigfig.fragroute_ascii, 'fragroute --help', 'fragroute')
    if function=='snort':
        scriptRun(bigfig.snort_ascii, 'snort --help', 'snort')
    if function=='nikto':
        scriptRun(bigfig.nikto_ascii, 'penbang/netkit/nikto/nikto-2.1.5/nikto.pl --help', 'penbang/netkit/nikto/nikto-2.1.5/nikto.pl')
    if function=='ophcrack-cli':
        scriptRun(bigfig.ophcrack_ascii, 'ophcrack-cli --help', 'ophcrack-cli')
    if function=='spike':
        scriptRun(bigfig.spike_ascii, 'pen_spike -help', 'pen_spike')
    if function=='callerpy':
        scriptRun(bigfig.callerpy_ascii, 'penbang/netkit/callerpy/callerpy.py -help', 'penbang/netkit/callerpy/callerpy.py')
    if function=='wpscan':
        scriptRun(' ', 'ruby penbang/netkit/wpscan/wpscan/wpscan.rb', 'ruby penbang/netkit/wpscan/wpscan/wpscan.rb')
    if function=='wpstools':
        scriptRun(' ', 'ruby penbang/netkit/wpscan/wpscan/wpstools.rb', 'ruby penbang/netkit/wpscan/wpscan/wpstools.rb')
    if function=='w3af_cli':
        scriptRun(bigfig.w3af_ascii, 'python penbang/netkit/w3af/w3af_console --help', 'penbang/netkit/w3af/w3af_console')
    if function=='tor-arm':
        scriptRun(' ', 'arm --help', 'arm')
    if function=='patator':
        scriptRun(bigfig.patator_ascii, 'penbang/netkit/patator/patator_v0.5.py --help', 'penbang/netkit/patator/patator_v0.5.py')
    if function=='patator-tor':
        scriptRun(bigfig.patator_tor_ascii, 'penbang/netkit/patator/patator_tor.py --help', 'penbang/netkit/patator/patator_tor.py')        
    else:
        print "Error"

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\033[32mEXIT PENBANG LAUNCHER\033[0m"
        pass

