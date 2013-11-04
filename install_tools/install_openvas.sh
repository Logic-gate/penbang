#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)


echo 'openvas installation script'
echo 'Downloading build dependencies'
sudo apt-get update
sudo apt-get install libssh-dev
sudo apt-get install libssh-4 #WHY??????
sudo apt-get install gnutls-dev
sudo apt-get install libglib2.0-dev
sudo apt-get install libpcap-dev
sudo apt-get install libgpgme11-dev
sudo apt-get install uuid-dev
sudo apt-get install bison
sudo apt-get install pkg-config
sudo apt-get install libksba8
sudo apt-get install libqt4-dev
sudo apt-get install libsqlite3-dev
sudo apt-get install libxml2-dev
sudo apt-get install libxslt1-dev
sudo apt-get install xsltproc
sudo apt-get install cmake
sudo apt-get install build-essential
sudo apt-get install libldap2-dev
sudo apt-get install libmicrohttpd5
sudo apt-get install libmicrohttpd-dev
sudo apt-get install doxygen
sudo apt-get install xmltoman
sudo apt-get install sqlfairy

echo 'Downloading openvas-lib'
wget -P /home/$(whoami)/penbang/netkit/openvas/lib/ http://wald.intevation.org/frs/download.php/1303/openvas-libraries-6.0.0.tar.gz

echo 'Downloading openvas-cli'
wget -P /home/$(whoami)/penbang/netkit/openvas/cli/ http://wald.intevation.org/frs/download.php/1323/openvas-cli-1.2.0.tar.gz

echo 'Downloading openvas-manager'
wget -P /home/$(whoami)/penbang/netkit/openvas/manager/ http://wald.intevation.org/frs/download.php/1311/openvas-manager-4.0.0.tar.gz

echo 'Downloading openvas-scanner'
wget -P /home/$(whoami)/penbang/netkit/openvas/scan/ http://wald.intevation.org/frs/download.php/1307/openvas-scanner-3.4.0.tar.gz

echo 'Downloading openvas-administrator'
hwget -P /home/$(whoami)/penbang/netkit/openvas/admin/ http://wald.intevation.org/frs/download.php/1319/openvas-administrator-1.3.0.tar.gz

echo 'Downloading gsd'
wget -P /home/$(whoami)/penbang/netkit/openvas/gsd/ http://wald.intevation.org/frs/download.php/1084/gsd-1.2.2.tar.gz

echo 'Downloading gsa'
wget -P /home/$(whoami)/penbang/netkit/openvas/gsa/ http://wald.intevation.org/frs/download.php/1315/greenbone-security-assistant-4.0.0.tar.gz

#building
chmod +x /home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building Lib'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/lib/openvas-libraries-6.0.0.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/lib/openvas-libraries-6.0.0
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building cli'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/cli/openvas-cli-1.2.0.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/cli/openvas-cli-1.2.0
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building Manager'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/manager/openvas-manager-4.0.0.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/manager/openvas-manager-4.0.0
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building Scanner'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/scan/openvas-scanner-3.4.0.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/scan/openvas-scanner-3.4.0
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building Administrator'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/admin/openvas-administrator-1.3.0.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/admin/openvas-administrator-1.3.0
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building GSD'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/gsd/gsd-1.2.2.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/gsd/gsd-1.2.2
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

echo 'Building GSA'
tar xfvz /home/$(whoami)/penbang/netkit/openvas/gsa/greenbone-security-assistant-4.0.0.tar.gz
cd /home/$(whoami)/penbang/netkit/openvas/gsd/greenbone-security-assistant-4.0.0
sudo cmake .
sudo make doc-full
sudo make
sudo make install

echo 'Checking...'
./home/$(whoami)/projects/penbang/netkit/openvas/openvas-check-setup

#echo 'Adding user'
#sudo openvas-adduser
#echo 'Creating Cert'
#sudo openvas-mkcert
#echo 'Fetching latest nvt'
#sudo openvas-nvt-sync
#echo 'Manager Setup'
#echo
#echo 'Creating Client Cert'
#echo
#echo -n 'Enter commonName: '
#read commonName
#sudo openvas-mkcert-client -n $commonName -i
#echo 'Rebuilding Manager...Please wait this may take some time'
#sudo openvasmd --rebuild
#echo 'Administrator Setup'
#echo 'Creating Admin User'
#echo -n 'Enter username: '
#read username
#openvasad -c 'add_user' -n $username -r Admin

exit 0

