#!/bin/bash
set -ex

# iosxr -> cisco.iosxr.iosxr
grep -RiIl 'ansible_network_os' | xargs perl -i -pe "s/'iosxr'/'cisco.iosxr.iosxr'/g"

# junos -> junipernetworks.junos.junos
grep -RiIl 'ansible_network_os' | xargs perl -i -pe "s/'junos'/'junipernetworks.junos.junos'/g"
