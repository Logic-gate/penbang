#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'Patator installation script'
echo 'Downloading patator'
wget -P /home/$(whoami)/penbang/netkit/patator/ https://patator.googlecode.com/files/patator_v0.5.py

exit 0