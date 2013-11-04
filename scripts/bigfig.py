#Place the script header and any additional info here. 
#Call it by bigfig.example_ascii in Scripts.py


john_ascii = '''

 o          
 |  _ |_ __ 
_| (_)| || |

	John the Ripper password cracker
'''

cdp_ascii = '''
       _ 
 _  _||_)
(_ (_||  packet generator


'''

file2cable_ascii = '''
  _         __                
_|_ o  |  _  _) _  _ |_  |  _ 
 |  |  | (/_/__(_ (_||_) | (/_
	
-v verbose (hex dump to screen)
-i <int> interface
-f <file> the file you want to send
'''

igrp_ascii = '''
    _     _ 
 o (_| __|_)
 | __| | |   route injector

'''

ass_ascii = '''
 _           __       __
|_|         (_       (_ 
| |utonomous __)ystem __)anner     

'''

irdp_ascii = '''
          _ 
 o  __ _||_)
 |  | (_||  

'''

irdpresponder_ascii = '''
          _  _        _                
 o  __ _||_)|_) _  _ |_) _ __  _| _  __
 |  | (_||  | \(/__> |  (_)| |(_|(/_ | 

'''

itrace_ascii = '''
 o _|_ __ _  _  _ 
 |  |_ | (_|(_ (/_

'''
tctrace_ascii = '''

_|_ _ _|_ __ _  _  _ 
 |_(_  |_ | (_|(_ (/_

'''

netenum_ascii = '''

__  _ _|_ _ __    __ 
| |(/_ |_(/_| ||_||||

verbosity = ['0', '1', '2', '3']
timeout = (seconds)

e.g.

192.168.1.1/24 9 3
any ip that does not respond within 9 seconds is considered down.
verbosity is set to maximum

'''
protos_ascii = '''
 _              __
|_)_|_ _  __ _ (_ 
|   |_(_) | (_)__)

'''

nmap_ascii = '''
          _ 
__ __  _ |_)
| ||||(_||  

'''

hsrp_ascii = '''

|_  _  __|_)
| |_>  | |  

'''

tcpdump_ascii = '''

       _           _ 
_|_ _ |_) _|   __ |_)
 |_(_ |  (_||_|||||  

'''
dfkaa_ascii = '''
     _         
 _|_|_ |  _  _ 
(_| |  |<(_|(_|

'''

tshark_ascii = '''
_|_ _ |_  _  __ | 
 |__> | |(_| |  |<

'''

aircrack_ascii = '''
                               _ 
 _  o  __ _  __ _  _  | ---__ (_|
(_| |  | (_  | (_|(_  |<   | |__|

Dont forget airmon-ng
'''

reaver_ascii = '''
 __ _  _     _  __
 | (/_(_|\_/(/_ | 

'''


airodump_ascii = '''
                      _        _ 
 _  o  __ _  _|   __ |_)---__ (_|
(_| |  | (_)(_||_|||||     | |__|

Dont forget airmon-ng
'''

airmon_ascii = '''
                         _ 
 _  o  ____  _ __ ---__ (_|
(_| |  | |||(_)| |   | |__|

'''

sslsniff_ascii = '''
 __ __    __   ___ __ __
(_ (_ |  (_ |\| | |_ |_ 
__)__)|____)| |_|_|  |  

'''

sslstrip_ascii = '''
 __ __    _____ _ ___ _ 
(_ (_ |  (_  | |_) | |_)
__)__)|____) | | \_|_|  

'''

dsniff_ascii = '''
 _  __   ___ __ __
| \(_ |\| | |_ |_ 
|_/__)| |_|_|  |  

'''


kismet_ascii = '''
   ___ __    _____
|/  | (_ |V||_  | 
|\ _|___)| ||__ | 

If, for some reason Kismet refuses to start or raises an error\nTry recompiling it from penbang dir
Hit Enter(empty string) to launch kismet curses\n Ctrl-d to exit
'''

filesnarf_ascii = '''
 _____    __ __    _  _  __
|_  | |  |_ (_ |\||_||_)|_ 
|  _|_|__|____)| || || \|  

'''

mailsnarf_ascii = '''
    _ ___    __    _  _  __
|V||_| | |  (_ |\||_||_)|_ 
| || |_|_|____)| || || \|  

'''
urlsnarf_ascii = '''
    _     __    _  _  __
| ||_)|  (_ |\||_||_)|_ 
|_|| \|____)| || || \|  

'''
msgsnarf_ascii = '''
    __ __ __    _  _  __
|V|(_ /__(_ |\||_||_)|_ 
| |__)\_|__)| || || \|  

'''

webspy_ascii = '''
    __ _  __ _ \ /
| ||_ |_)(_ |_) Y 
|^||__|_)__)|   | 

'''

arpspoof_ascii = '''
       _     _         _
 _  __|_) _ |_) _  _ _|_
(_| | |  _> |  (_)(_) | 

'''
dnsspoof_ascii = '''
             _         _
 _|__  _  _ |_) _  _ _|_
(_|| |_> _> |  (_)(_) | 

'''

macof_ascii = '''
              _
__  _  _  _ _|_
|||(_|(_ (_) | 

'''

sshmitm_ascii = '''
 __ __      ______   
(_ (_ |_||V| |  | |V|
__)__)| || |_|_ | | |

'''

webmitm_ascii = '''
    _ |_ __  o _|___ 
\^/(/_|_)||| |  |_|||

'''

subterfuge_ascii = '''
 __                 _    _    
(_    |_ _|_ _  ___|_   (_| _ 
__)|_||_) |_(/_ |  | |_|__|(/_

Hit Enter(empty string) to start it with the default ip:port
default: 127.0.0.1:80
If you have apache or any other webserver, change the port.
'''

ettercap_ascii = '''
 ________ __ _  __ _  _ 
|_  |  | |_ |_)/  |_||_)
|__ |  | |__| \\__| ||  

--gtk for GUI
'''
nessus_ascii = '''

    __ __ __    __
|\||_ (_ (_ | |(_ 
| ||____)__)|_|__)

The default port is 8834
'''

sqlninja_ascii = '''
 __ _              o  _ 
(_ (_| | |\| o |\| | |_|
__)  | | | | | | |_| | |

'''

etherape_ascii = '''
 __                _    
|_ _|_|_  _  __ _ |_) _ 
|__ |_| |(/_ | (_||  (/_

'''

wfuzz_ascii = '''
    __      ___
| ||_     _  _/
|^||  |_| /_/__

'''

hydra_ascii = '''
          _    
|_| \/ _||_) _ 
| | / (_|| \(_|

'''

findmyhash_ascii = '''

  _            \ /       __   
_|_ o __  _||V| Y |_  _ (_ |_ 
 |  | | |(_|| | | | |(_|__)| |

'''

parselog_ascii = '''

 _        __          _ 
|_) _  __(_  _ |   _ (_|
|  (_| | __)(/_|__(_)__|

	By z3ros3c@gmail.com
	
	penbang version

	This file parses the sslstrip.log created by
	sslstrip for usernames and passwords (and other
	interesting information) defined in the file
	def.txt. It will also
	give you a complete list of all unknown information,
	with the exception of anything listed in the file
	blacklist.txt

  Usage:

    parselog$ input output
  
    output  [default path is penbang/netkit/SMITM/parse/output.accounts]

'''

w3af_ascii = '''
      __  _   _
| || |__)|_|_|_
|_||_|__)| | | 

'''
patator_ascii = '''
 _                   
|_) _ _|_ _ _|_ _  __
|  (_| |_(_| |_(_) | 


'''

nikto_ascii = '''




'''

ntop_ascii = '''


'''

arping_ascii = '''


'''
callerpy_ascii = '''
 __                _    
/   _  |  |  _  __|_) \/
\__(_| |  | (/_ | |   / 

'''

patator_tor_ascii = '''
 _                   
|_) _ _|_ _ _|_ _  __
|  (_| |_(_| |_(_) | 


'''

sqlsus_ascii = '''



'''