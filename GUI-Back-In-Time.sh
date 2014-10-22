#! /bin/bash

sshfs -p 22122 ebaumeis@141.213.4.160:/share/homes/ebaumeis /media/Backup
backintime-gnome
sudo umount /media/Backup
