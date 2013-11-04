#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'argus installation script'
wget -P /home/$(whoami)/penbang/netkit/argus/ http://http.kali.org/pool/main/a/argus/argus-server_2.0.6.fixes.1-16.3_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/argus/argus-server_2.0.6.fixes.1-16.3_i386.deb
exit 0
