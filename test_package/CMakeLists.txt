cmake_minimum_required(VERSION 3.15)

set(CMAKE_TOOLCHAIN_FILE build/conan_toolchain.cmake)

project(test_package C CXX)

find_package(raspberry_pi_pico_sdk REQUIRED)

add_executable(test_package main.cpp)

target_link_libraries(test_package raspberry_pi_pico_sdk::raspberry_pi_pico_sdk)

