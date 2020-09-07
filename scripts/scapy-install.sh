#!/bin/bash

set -e

apt update
apt install -y libproj-dev proj-data proj-bin python3-pip

pip3 install --pre scapy[complete]
