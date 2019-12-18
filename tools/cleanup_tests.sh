#!/bin/bash
set -ex

# httpapi -> ansible.netcommon.httpapi
grep -RiIl 'httpapi' | xargs perl -i -pe 's/((ansible_)?connection)(.*)((?<!_|\.)httpapi)/\1\3ansible.netcommon.\4/g' | true
# network_cli -> ansible.netcommon.network_cli
grep -RiIl 'network_cli' | xargs perl -i -pe 's/((ansible_)?connection)(.*)((?<!_|\.)network_cli)/\1\3ansible.netcommon.\4/g' | true
# cisco.netcommon.network_cli -> ansible.netcommon.network_cli
# TODO(pabelager): This is a bug in migrate.py, we should fix it
grep -RiIl 'cisco.netcommon.network_cli' | xargs perl -i -pe 's/cisco.netcommon.network_cli/ansible.netcommon.network_cli/g' | true
