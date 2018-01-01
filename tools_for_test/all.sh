#!/bin/sh
sudo sendip -p ipv6 -p icmp -d 'i love u' ::1
sudo sendip -p ipv4 -d "i love u" 127.0.0.1
sudo sendip -p ipv6 -p tcp -ts 80 -td 9000 -d 'i love u' ::1
sudo sendip -p ipv6 -p udp -us 80 -ud 9000 -d 'i love u' ::1
sudo sendip -p ipv4 -p icmp -cc 8034243 -cd 67 -d 'i love u' -v www.liquor233.cn
sudo sendip -p ipv6 -d "i love u" ::1
sudo sendip -p ipv4 -p tcp -ts 80 -td 9000 -d 'i love u' -v www.liquor233.cn
sudo sendip -p ipv4 -p udp -us 80 -ud 9000 -d 'i love u' -v www.liquor233.cn
