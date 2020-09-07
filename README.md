# scapy-utils
Install scripts and examples for https://github.com/secdev/scapy

## General requirements

Scapy needs Python (preferable Py3) and pcap | npcap | tcpdump to work.

Depending on how you run scapy, is better to have at least 2 GB RAM.

Scapy can eat all the memory if the packet responses are returned in a variable for further usage.

Scapy needs to be run with administrative privileges.

## Installation on Ubuntu 18.04

See installation script: [scripts/scapy-install.sh](scripts/scapy-install.sh).


## Installation on Windows 2012 R2
npcap need to be manually installed: https://nmap.org/npcap/dist/npcap-0.9997.exe

See installation script: [scripts/scapy-install.ps1](scripts/scapy-install.ps1).
The installation script assumes Cloudbase-Init is installed at path: `C:\Program Files\Cloudbase Solutions\Cloudbase-Init`

## Examples

```bash

python src/run-scapy-tests.py --help
usage: run-scapy-tests.py [-h] --target TARGET [--test_type {ICMP}]
                          [--max_packets MAX_PACKETS]
                          [--return_packets {True,False}]
                          [--fuzz {True,False}]

optional arguments:
  -h, --help            show this help message and exit
  --target TARGET       The target of the test. Should be a valid IPv4 address
  --test_type {ICMP}    Test type to perform
  --max_packets MAX_PACKETS
                        Maximum packets to send
  --return_packets {True,False}
                        Whether to return and show packet responses
  --fuzz {True,False}   Whether to fuzz the test type packets



# execute the command with administrative privileges
# "192.168.100.81" is the IP of the target instance under test (DUT)

# Run a basic ICMP test
python src/run-scapy-tests.py "192.168.100.81" "ICMP"

# Run an ICMP fuzzed test with 10 sent packets without showing returned packets
python src/run-scapy-tests.py "192.168.100.81" --test_type "ICMP" \
    --max_packets 10 --return_packets False --fuzz True

```

