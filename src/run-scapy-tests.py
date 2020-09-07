#!/usr/bin/env python

import sys
from scapy.all import *


def run_scapy(target_ip):
    packets = send(IP(dst=target_ip)/ICMP(), return_packets=True)
    packets.show()

run_scapy(sys.argv[1])
