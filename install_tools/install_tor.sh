#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'Tor installation script'
echo 'Downloading tor'
wget -P /home/$(whoami)/penbang/netkit/tor/ https://www.torproject.org/dist/torbrowser/linux/tor-browser-gnu-linux-i686-2.3.25-13-dev-en-US.tar.gz

cd /home/$(whoami)/penbang/netkit/tor/
echo 'unpacking'
tar -xvzf tor-browser-gnu-linux-i686-2.3.25-13-dev-en-US.tar.gz

echo 'Installing Tor-Arm'
sudo apt-get install tor-arm

exit 0