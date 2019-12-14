#!/bin/bash
set -ex

# network_cli -> ansible.netcommon.network_cli
grep -RiIl 'network_cli' | xargs sed -i 's/\(connection\)\(.*\)\(network_cli\)/\1\2ansible.netcommon.\3/g'
