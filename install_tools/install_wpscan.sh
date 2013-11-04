#!/bin/bash

#Report any issues with this script to <mad_dev@linuxmail.org>

#Tested on crunchbang waldorf(openbox)

sudo apt-get install libcurl4-gnutls-dev libopenssl-ruby libxml2 libxml2-dev libxslt1-dev ruby-dev

cd /home/$(whoami)/penbang/netkit/wpscan

git clone https://github.com/wpscanteam/wpscan.git

cd wpscan

sudo gem install bundler && bundle install --without test development

exit 0