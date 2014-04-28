#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'arping installation script'
wget -P /home/$(whoami)/penbang/netkit/arping/ http://http.kali.org/pool/main/a/arping/arping_2.11-1_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/arping/arping_2.11-1_i386.deb

exit 0
