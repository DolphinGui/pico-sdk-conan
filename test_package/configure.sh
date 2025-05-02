#!/usr/bin/sh

set -ex

mkdir -p build
conan install . -pr:h=../profiles/rp2350 -pr:h=arm-gcc-12.3 --build=missing -of build
cd build
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=MinSizeRel -DCMAKE_EXPORT_COMPILE_COMMANDS=On
cd ..




