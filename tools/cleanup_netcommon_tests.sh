#!/bin/bash
set -ex

# iosxr -> cisco.iosxr.iosxr
grep -RiIl 'ansible_network_os' | xargs perl -i -pe "s/'iosxr'/'cisco.iosxr.iosxr'/g"
