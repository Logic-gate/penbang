#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

# For non-penbang users change the path after -P

echo 'Callerpy installation script'
wget -P /home/$(whoami)/penbang/netkit/callerpy/ http://penbang.sysbase.org/scripts/0.0.3/callerpy/callerpy.py
dos2unix /home/$(whoami)/penbang/netkit/callerpy/callerpy.py
cd /home/$(whoami)/penbang/netkit/callerpy/
sudo chmod +x /home/$(whoami)/penbang/netkit/callerpy/callerpy.py
wget -P /home/$(whoami)/penbang/netkit/callerpy/ http://penbang.sysbase.org/scripts/0.0.3/callerpy/auth.py
wget -P /home/$(whoami)/penbang/netkit/callerpy/ http://penbang.sysbase.org/scripts/0.0.3/callerpy/urlRedirect.py
wget -P /home/$(whoami)/penbang/netkit/callerpy/ http://penbang.sysbase.org/scripts/0.0.3/callerpy/history.log
wget -P /home/$(whoami)/penbang/netkit/callerpy/ http://penbang.sysbase.org/scripts/0.0.3/callerpy/twill_output
wget -P /home/$(whoami)/penbang/netkit/callerpy/ http://penbang.sysbase.org/scripts/0.0.3/callerpy/cookie_session_twitter
#Precautionary measure
dos2unix /home/$(whoami)/penbang/netkit/callerpy/auth.py
dos2unix /home/$(whoami)/penbang/netkit/callerpy/urlRedirect.py

exit 0
