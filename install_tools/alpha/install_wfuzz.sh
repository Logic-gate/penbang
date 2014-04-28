#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

echo 'wfuzz installation script'
wget -P /home/$(whoami)/penbang/netkit/wfuzz/ http://http.kali.org/pool/main/w/wfuzz/wfuzz_2.0-1kali1_all.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/wfuzz/wfuzz_2.0-1kali1_all.deb

exit 0
