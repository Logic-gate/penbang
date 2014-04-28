#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'Metasploit installation script'
echo 'Downloading Metasploit 32 bit'
wget -P /home/$(whoami)/penbang/netkit/metasploit/ http://downloads.metasploit.com/data/releases/metasploit-latest-linux-installer.run
echo 'Runing...'
chmod +x /home/$(whoami)/penbang/netkit/metasploit/metasploit-latest-linux-installer.run
sudo /home/$(whoami)/penbang/netkit/metasploit/metasploit-latest-linux-installer.run
#firefox --new-instance http://www.rapid7.com/products/metasploit/download-thank-you.jsp

exit 0
