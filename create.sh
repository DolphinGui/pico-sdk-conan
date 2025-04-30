#!/usr/bin/sh

set -ex

conan create . -pr:b=default  -pr:h=arm-gcc-12.3 -pr:h=./profiles/rp2350 -v

