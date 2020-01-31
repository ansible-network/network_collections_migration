#!/bin/bash
set -ex

# Fix yaml quotes
grep -RiIl 'Dependency' | xargs perl -i -pe "s/- 'Dependency: ''feature bfd'''/- \"Dependency: ''feature bfd''\"/g"
