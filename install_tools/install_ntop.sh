#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'ears installation script'
wget -P /home/$(whoami)/penbang/netkit/ntop/ http://http.kali.org/pool/main/n/ntop/ntop_4.99.3+ndpi5517+dfsg3-1_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/ntop/ntop_4.99.3+ndpi5517+dfsg3-1_i386.deb

exit 0
