#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'Armitage installation script'
echo 'downloading Armitage'
#wget -P /home/$(whoami)/penbang/netkit/armitage/ http://www.fastandeasyhacking.com/download/armitage041013.tgz Wget fails to download. Package included in release
tar xfvz /home/$(whoami)/penbang/netkit/armitage/armitage041013.tgz
cp /home/$(whoami)/penbang/netkit/armitage/armitage_path /home/$(whoami)/penbang/netkit/armitage/armitage/armitage
cd /usr/local/bin/
sudo ln -s /home/$(whoami)/penbang/netkit/armitage/armitage/armitage
exit 0
