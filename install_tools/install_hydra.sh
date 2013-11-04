#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>
#
#Tested on crunchbang waldorf(openbox)

echo 'hyfra installation script'
echo 'Downloading build dependencies'
wget -P /home/$(whoami)/penbang/netkit/hydra/ http://http.kali.org/pool/main/a/afpfs-ng/libafpclient0_0.8.1-5_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/hydra/libafpclient0_0.8.1-5_i386.deb
wget -P /home/$(whoami)/penbang/netkit/hydra/ http://http.kali.org/pool/main/a/afpfs-ng/libafpclient-dev_0.8.1-5_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/hydra/libafpclient-dev_0.8.1-5_i386.deb
wget -P /home/$(whoami)/penbang/netkit/hydra/ http://http.kali.org/pool/main/h/hydra/hydra_7.4.2-2kali0_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/hydra/hydra_7.4.2-2kali0_i386.deb #This will take care of some deps
wget -P /home/$(whoami)/penbang/netkit/hydra/ http://http.kali.org/pool/main/h/hydra/hydra-gtk_7.4.2-2kali0_i386.deb
gdebi-gtk /home/$(whoami)/penbang/netkit/hydra/hydra-gtk_7.4.2-2kali0_i386.deb
exit 0
