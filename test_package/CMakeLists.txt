cmake_minimum_required(VERSION 3.15)
set(CMAKE_EXECUTABLE_SUFFIX_ASM .elf)
set(CMAKE_EXECUTABLE_SUFFIX_C .elf)
set(CMAKE_EXECUTABLE_SUFFIX_CXX .elf)
set(PICO_CXX_ENABLE_EXCEPTIONS On)

include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

project(raspberry_pico_test C CXX ASM)

pico_sdk_init()
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_executable(main main.cpp)

target_compile_options(main PRIVATE -Wall -Werror)
target_link_libraries(main pico_stdlib hardware_gpio)

pico_add_extra_outputs(main)
pico_enable_stdio_usb(main 1)
pico_enable_stdio_uart(main 0)
