# Copyright 2020 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import argparse

import scapy.all as scapy


def run_scapy(target, test_type, max_packets, return_packets, fuzz):
    packet_type = scapy.ICMP()
    if fuzz:
        packet_type = scapy.fuzz(packet_type)
    packet_gen = scapy.IP(dst=target)/packet_type
    packets = scapy.send(
        packet_gen,
        return_packets=return_packets,
        verbose=not return_packets,
        count=max_packets)

    if return_packets:
        packets.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--target',
        help='The target of the test. Should be a valid IPv4 address',
        required=True)
    parser.add_argument(
        '--test_type',
        help='Test type to perform',
        default="ICMP",
        choices=["ICMP"])
    parser.add_argument(
        '--max_packets',
        help='Maximum packets to send',
        type=int,
        default=1)
    parser.add_argument(
        '--return_packets',
        help='Whether to return and show packet responses',
        type=eval,
        choices=[True, False],
        default=True)
    parser.add_argument(
        '--fuzz',
        help='Whether to fuzz the test type packets',
        type=eval,
        choices=[True, False],
        default=True)

    args = vars(parser.parse_args())

    run_scapy(**args)


if __name__ == "__main__":
    main()
