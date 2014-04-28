#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'ettercap installation script'
echo 'Downloading ettercap'
wget -P /home/$(whoami)/penbang/netkit/ettercap/ http://downloads.sourceforge.net/project/ettercap/ettercap/0.7.6-Locard/ettercap-0.7.6.tar.gz
echo 'Downloading build dependencies'
sudo apt-get update
sudo apt-get install libnet1-dev
sudo apt-get install libnet6-1.3-dev
sudo apt-get install libpthread-stubs0-dev
sudo apt-get install libpthread-workqueue-dev
sudo apt-get install zlibc
sudo apt-get install libtool
sudo apt-get install automake
sudo apt-get install flex
sudo apt-get install bison
sudo apt-get install libssl-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libncurses5-dev
sudo apt-get install libpcre3-dev
sudo apt-get install cmake
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libltdl-dev
echo 'unpacking'
cd /home/$(whoami)/penbang/netkit/ettercap
sudo tar -xzf ettercap-0.7.6.tar.gz
echo 'making build'
cd ettercap-0.7.6
sudo mkdir build
cd build
sudo cmake ../
sudo make
sudo make install
exit 0
