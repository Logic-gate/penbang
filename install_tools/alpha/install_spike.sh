#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'spike installation script'
wget -P /home/$(whoami)/penbang/netkit/spike/ http://http.kali.org/pool/main/s/spike/spike_2.9-1kali1_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/spike/spike_2.9-1kali1_i386.deb

exit 0
