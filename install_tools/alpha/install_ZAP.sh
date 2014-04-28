#!/bin/bash

echo 'Downloading OWASP ZAP'

wget -P /home/$(whoami)/penbang/netkit/ZAP/ https://zaproxy.googlecode.com/files/ZAP_2.2.2_Linux.tar.gz

echo 'Unpacking'

cd /home/$(whoami)/penbang/netkit/ZAP/

tar -xvzf "/home/$(whoami)/penbang/netkit/ZAP/ZAP_2.2.2._Linux.tar.gz"


exit 0