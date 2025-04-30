#!/usr/bin/sh

mkdir -p build
cd build
conan install .. -pr:h=../../profiles/rp2350 -pr:h=arm-gcc-12.3 --build=raspberry_pi_pico_sdk/2.1.1
cd ..
