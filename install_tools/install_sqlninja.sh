#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>
#
#Tested on crunchbang waldorf(openbox)

echo 'sqlninga installation script'
echo 'Downloading sqlninja'
wget -P /home/$(whoami)/penbang/netkit/sqlninja/ http://http.kali.org/pool/main/s/sqlninja/sqlninja_0.2.6-r1-1kali0_all.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/sqlninja/sqlninja_0.2.6-r1-1kali0_all.deb

exit 0
