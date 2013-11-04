#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'ophcrack installation script'
wget -P /home/$(whoami)/penbang/netkit/ophcrack/ http://http.kali.org/pool/main/o/ophcrack/ophcrack_3.4.0-2_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/ophcrack/ophcrack_3.4.0-2_i386.deb
wget -P /home/$(whoami)/penbang/netkit/ophcrack/ http://http.kali.org/pool/main/o/ophcrack/ophcrack-cli_3.4.0-2_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/ophcrack/ophcrack-cli_3.4.0-2_i386.deb

exit 0
