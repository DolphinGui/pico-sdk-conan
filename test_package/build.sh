#!/usr/bin/sh

set -ex


conan install . -pr:h=../profiles/rp2350 -pr:h=arm-gcc-12.3 --build=missing -of build
conan build . -pr:h=../profiles/rp2350 -pr:h=arm-gcc-12.3 -of build
