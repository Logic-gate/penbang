#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'subterfuge installation script'
echo 'downloading subterfuge'
wget -P /home/$(whoami)/penbang/netkit/subterfuge/ http://subterfuge.googlecode.com/files/SubterfugePublicBeta5.0.tar.gz
echo 'Downloading build dependencies'
sudo apt-get install python-tk
cd /home/$(whoami)/penbang/netkit/subterfuge/
tar xfvz SubterfugePublicBeta5.0.tar.gz
cd subterfuge
sudo python install.py


exit 0
