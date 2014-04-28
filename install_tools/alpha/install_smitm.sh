#!/bin/bash


echo 'Silent MITM'


sudo mv netkit/SMITM/smitm /usr/local/bin
sudo mv netkit/SMITM/smitm-stop /usr/local/bin
sudo mv netkit/SMITM/parselog /usr/local/bin
sudo mv netkit/SMITM/log_ex /usr/local/bin
chmod +x /usr/local/bin/parselog
chmod +x /usr/local/bin/log_ex

echo 'done'

exit 0
