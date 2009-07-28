#!/bin/sh

#rm -rf command-not-found-*

#svn export command-not-found command-not-found-$1
#mkdir command-not-found-$1/data

#cd command-not-found-$1/data
#sudo python ../src/generate.py
#cd

tar cvjf command-not-found-$1.tar.bz2 command-not-found-$1

sha1sum command-not-found-$1.tar.bz2
scp command-not-found-$1.tar.bz2 ozan@cekirdek.pardus.org.tr:public_html/dist/sources

