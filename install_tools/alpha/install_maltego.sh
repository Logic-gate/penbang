#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)


wget -P /home/$(whoami)/penbang/netkit/maltego/ http://www.paterva.com/malv32/community/maltego-radium-CE.community-2012-12-20.deb
sudo gdebi-gtk /home/$(whoami)/penbang/netkit/maltego/maltego-radium-CE.community-2012-12-20.deb

exit 0
