
The project was hosted on https://sourceforge.net/projects/penbang/

The repo is up, however it is not functioning.

Here is a summary:

OLD

penbang_install_script.py ---> Request script from server(penbang.sysbase.org)
			|					|
			|					|
			|					Get install_tool.sh ---> Run install_tool.sh
			|												      |
			|                                                     Deploy in penbang/netkit/tool
            |
           for every tool; create penbang/netkit/tool dir


NEW "GIT REPO" (not implemented)

penbang_install_script.py ---> call script from install_tools/install_tool.sh
			|
			|
			for every tool; create penbang/netkit/tool dir 

This way we only need to change where to get the scripts, rather than changing the paths in install_tool.sh



NOTES:

Scripts.py and bigfig.py will always be to the latest version

TODO::

Rewrite install_penbang_update.sh ----> is is needed??? there is a repo.

Rewrite penbang_install_script.py ----> must include the initial install.py(irpas, dsniff....)

add missing tools in bigfig.py ----> or the hell with it!!!

Write a seperate script for the menu --- Thank you ryan

Rewrite Readme.txt

::

I included a netkit dir in the repo; it has the following:

! - spike/pen_spkie ---> a spike launcher I wrote
! - SMITM ---> Silent Man In The Middle (https://sourceforge.net/p/penbang/wiki/Home/)
! - openvas-check-script
! - Hash_ID
! - crunch
! - armitage source and armitage_path(mad_dev is hard coded?????)
! - common.mak (a fix for aircrack)

Hopefully within the next 2-3 days everthing will up and running.

For the life of me, I have no idea why I didn't start a repo  