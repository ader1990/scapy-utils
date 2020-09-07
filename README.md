# scapy-utils
Install scripts and examples for https://github.com/secdev/scapy

## General requirements

Scapy needs Python (preferable Py3) and pcap | ncap | tcpdump to work.

Depending on how you run scapy, is better to have at least 2 GB RAM.

Scapy can eat all the memory if the packet responses are returned in a variable for further usage.

Scapy needs to be run with administrative privileges.

How to run:

```bash
    # execute the command with administrative privileges
    # "192.168.100.81" is the IP of the target instance under test (DUT)

    # Run a basic ICMP test
    python src/run-scapy-tests.py "192.168.100.81" "icmp"

    # Run a fuzzed ICMP test
    python src/run-scapy-tests.py "192.168.100.81" "icmp" "fuzzy"
```

## Ubuntu 18.04

See installation script: [scripts/scapy-install.sh](scripts/scapy-install.sh).


## Windows 2012 R2
ncap is required: https://nmap.org/npcap/dist/npcap-0.9997.exe

See installation script: [scripts/scapy-install.ps1](scripts/scapy-install.ps1).
The installation script assumes Cloudbase-Init is installed at path: `C:\Program Files\Cloudbase Solutions\Cloudbase-Init`
