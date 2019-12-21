#!/bin/bash
set -ex

# mode: on -> mode: 'on'
grep -RiIl 'mode: on' | xargs perl -i -pe "s/(mode: )(on)/\1'\2'/"
