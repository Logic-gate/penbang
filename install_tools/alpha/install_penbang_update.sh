#!/bin/bash


#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

#Scripts.py
echo 'Changing Scripts.py'
cp /home/$(whoami)/penbang/netkit/netkit_source/Scripts.py /home/$(whoami)/penbang/netkit/netkit_source/Scripts_0.0.3.py
rm /home/$(whoami)/penbang/netkit/netkit_source/Scripts.py
wget -P /home/$(whoami)/penbang/ http://penbang.sysbase.org/scripts/0.5/mod_data/Scripts.py

#menu.xml
echo 'Changing menu.xml'
cp /home/$(whoami)/penbang/mod_data/openbox/menu.xml /home/$(whoami)/penbang/mod_data/openbox/menu_0.0.3_penbang.xml
rm /home/$(whoami)/penbang/mod_data/openbox/menu.xml
cp /home/$(whoami)/.config/openbox/menu.xml /home/$(whoami)/.config/openbox/menu_0.0.3_penbang.xml
rm /home/$(whoami)/.config/openbox/menu.xml
wget -P /home/$(whoami)/penbang/mod_data/openbox http://penbang.sysbase.org/scripts/0.5/mod_data/menu.xml


#bigfig.py
echo 'Changing bigfig.py'
cp /home/$(whoami)/penbang/netkit/netkit_source/bigfig.py /home/$(whoami)/penbang/netkit/netkit_source/bigfig_0.0.3.py
rm /home/$(whoami)/penbang/netkit/netkit_source/bigfig.py
wget -P /home/$(whoami)/penbang/ http://penbang.sysbase.org/scripts/0.5/mod_data/bigfig.py

#Readme.txt
echo 'Changing Readme.txt'
rm /home/$(whoami)/penbang/Readme.txt
wget -P /home/$(whoami)/penbang/ http://penbang.sysbase.org/install_tools/0.5/Readme.txt

#Precautionary measure
echo 'Converting Scripts.py and bigfig.py'
dos2unix /home/$(whoami)/penbang/Scripts.py
dos2unix /home/$(whoami)/penbang/bigfig.py

exit 0
