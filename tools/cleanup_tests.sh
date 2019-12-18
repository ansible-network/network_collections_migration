#!/bin/bash
set -ex

# httpapi -> ansible.netcommon.httpapi
grep -RiIl 'httpapi' | xargs perl -i -pe 's/((ansible_)?connection)(.*)((?<!_|\.)httpapi)/\1\3ansible.netcommon.\4/g' | true
# network_cli -> ansible.netcommon.network_cli
grep -RiIl 'network_cli' | xargs perl -i -pe 's/((ansible_)?connection)(.*)((?<!_|\.)network_cli)/\1\3ansible.netcommon.\4/g' | true
