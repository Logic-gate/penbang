#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'Snort installation script'
wget -P /home/$(whoami)/penbang/netkit/snort/ http://http.kali.org/pool/main/s/snort/snort_2.9.2.2-3_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/snort/snort_2.9.2.2-3_i386.deb

exit 0
