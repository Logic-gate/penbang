#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'nikto installation script'
wget -P /home/$(whoami)/penbang/netkit/nikto/ http://cirt.net/nikto/nikto-2.1.5.tar.gz
echo 'Downloading build dependencies'
sudo apt-get install perl
sudo apt-get install libwhisker2-perl
sudo apt-get install libapache-asp-perl
sudo apt-get install openssl
sudo perl -MCPAN -e 'install RPC::XML::Client'
sudo perl -MCPAN -e 'install RPC::XML'
cd /home/$(whoami)/penbang/netkit/nikto/
sudo tar -xvfz nikto-2.1.5.tar.gz
chmod +x /home/$(whoami)/penbang/netkit/nikto/nikto-2.1.5/nikto.pl
chmod +x /home/$(whoami)/penbang/netkit/nikto/nikto-2.1.5/replay.pl
exit 0
