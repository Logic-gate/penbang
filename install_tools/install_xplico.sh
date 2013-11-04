#!/bin/bash

#Lets hope this Works....


echo 'Downloading Xplico Deps'
sudo apt-get install tcpdump tshark apache2 php5 php5-sqlite build-essential perl libzip-dev libpcap-dev libsqlite3-dev php5-cli libapache2-mod-php5  libx11-dev libxt-dev libxaw7-dev python3.2 python3-httplib2 sqlite3 recode sox lame libnet1 libnet1-dev libmysqlclient-dev binfmt-support libssl-dev

wget -P /home/$(whoami)/penbang/netkit/xplico/ http://downloads.sourceforge.net/project/xplico/Xplico%20versions/version%201.0.1/xplico_1.0.1_i386.deb

gdebi-gtk /home/$(whoami)/penbang/netkit/xplico/xplico_1.0.1_i386.deb


exit 0