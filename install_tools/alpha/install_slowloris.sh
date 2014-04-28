#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'slowloris installation script'
wget -P /home/$(whoami)/penbang/netkit/slowloris/ http://ha.ckers.org/slowloris/slowloris.pl
wget -P /home/$(whoami)/penbang/netkit/slowloris/ http://ha.ckers.org/slowloris/slowloris6.pl
sudo perl -MCPAN -e 'install IO::Socket::INET'
sudo perl -MCPAN -e 'install IO::Socket::SSL'
sudo perl -MCPAN -e 'install IO::Socket::INET6'
sudo perl -MCPAN -e 'install IO::Socket::SSL'
sudo mv /home/$(whoami)/penbang/netkit/slowloris/slowloris.pl /usr/local/bin
sudo mv /home/$(whoami)/penbang/netkit/slowloris/slowloris6.pl /usr/local/bin
sudo chmod +x /usr/local/bin/slowloris.pl
sudo chmod +x /usr/local/bin/slowloris6.pl
exit 0
