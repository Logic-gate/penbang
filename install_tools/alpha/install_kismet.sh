#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'kismet installation script'
echo 'Downloading kismet'
wget -P /home/$(whoami)/penbang/netkit/kismet/ http://www.kismetwireless.net/code/kismet-2013-03-R1b.tar.xz
echo 'Downloading build dependencies'
sudo apt-get update
sudo apt-get install libatk1.0-0 #depends 
sudo apt-get install libc6 #depends
sudo apt-get install libexpat1 #depends
sudo apt-get install libgcc1 #depends
sudo apt-get install libgmp3-dev #depends
sudo apt-get install libmagickcore5 #depends
sudo apt-get install libncurses5 #depends
sudo apt-get install libpcap0.8 #depends
sudo apt-get install libstdc++6 #depends
sudo apt-get install zlib1g #depends
sudo apt-get install wireless-tools #depends
sudo apt-get install wireshark-common #depends
sudo apt-get install wget #suggest
sudo apt-get install sox #suggest
sudo apt-get install festival #suggest
sudo apt-get install gpsd #suggest
sudo apt-get install gsfonts #suggest
sudo apt-get install libwww-perl #suggest
sudo apt-get install libnl-dev #depend
echo 'unpacking'
cd /home/$(whoami)/penbang/netkit/kismet/
sudo tar -xvf kismet-2013-03-R1b.tar.xz
cd kismet-2013-03-R1b && ./configure
sudo make dep
sudo make sudoinstall
sudo make install
exit 0
