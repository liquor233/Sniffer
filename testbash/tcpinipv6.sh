#!/bin/sh
sudo sendip -p ipv6 -p tcp -ts 80 -td 9000 -d 'i love u' ::1
