#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'aircrack-ng installation script'
echo 'Downloading aircrack-ng'
wget -P /home/$(whoami)/penbang/netkit/aircrack-ng/source/ http://download.aircrack-ng.org/aircrack-ng-1.1.tar.gz
echo 'Downloading build dependencies'
sudo apt-get update
sudo apt-get install libpcap-dev
sudo apt-get install libssl-dev
sudo apt-get install build-essential
sudo apt-get install sqlite
sudo apt-get install iw
sudo apt-get install linux-headers-$(uname -r)
sudo apt-get install gcc
sudo apt-get install make
echo 'unpacking'
cd /home/$(whoami)/penbang/netkit/aircrack-ng/source
sudo tar xfvz aircrack-ng-1.1.tar.gz
sudo cp common.mak aircrack-ng-1.1/common.mak
echo 'compiling'
cd /home/$(whoami)/penbang/netkit/aircrack-ng/source/aircrack-ng-1.1 && sudo make && sudo make install
echo 'updating OUI'
sudo airodump-ng-oui-update

exit 0
