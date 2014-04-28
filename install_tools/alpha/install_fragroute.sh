#!/bin/bash


#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'fragroute installation script'
wget -P /home/$(whoami)/penbang/netkit/fragroute/ http://http.kali.org/pool/main/f/fragroute/fragroute_1.2-7.2kali1_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/fragroute/fragroute_1.2-7.2kali1_i386.deb

exit 0
