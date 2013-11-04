#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>
#
#Tested on crunchbang waldorf(openbox)

echo 'findmyhash installation script'
echo 'Downloading build dependencies'
sudo apt-get install libxml2
sudo apt-get install libxml2-dev
wget -P /home/$(whoami)/penbang/netkit/findmyhash/ http://http.kali.org/pool/main/f/findmyhash/findmyhash_1.1.2-1kali2_all.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/findmyhash/findmyhash_1.1.2-1kali2_all.deb

exit 0
