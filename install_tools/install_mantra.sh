#!/bin/bash



echo 'Downloading OWASP Mantra'

wget -P /home/$(whoami)/penbang/netkit/mantra/ http://downloads.sourceforge.net/project/getmantra/Mantra%20Security%20Toolkit/Janus%20-%200.92%20Beta/OWASP%20Mantra%20Janus%20Linux%2032.tar.gz

echo 'Unpacking'

cd /home/$(whoami)/penbang/netkit/mantra/

tar -xvzf "OWASP Mantra Janus Linux 32.tar.gz"

 ./"OWASP Mantra-0.92-Linux-x86-Install"

exit 0