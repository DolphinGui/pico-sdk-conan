cmake_minimum_required(VERSION 3.15)

include(${CMAKE_BINARY_DIR}/sdk/external/pico_sdk_import.cmake)

project(raspberry_pico_test C CXX ASM)

pico_sdk_init()
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_executable(main.elf main.cpp)

target_compile_options(main.elf PRIVATE -Wall -Werror)
target_link_libraries(main.elf pico_stdlib hardware_gpio)

# pico_add_extra_outputs(main)
pico_enable_stdio_usb(main.elf 1)
pico_enable_stdio_uart(main.elf 0)
