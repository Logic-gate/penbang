#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>
#
#Tested on crunchbang waldorf(openbox)

echo 'sqlsus installation script'
wget -P /home/$(whoami)/penbang/netkit/sqlsus/ http://http.kali.org/pool/main/s/sqlsus/sqlsus_0.7.2-1kali0_all.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/sqlsus/sqlsus_0.7.2-1kali0_all.deb

exit 0
