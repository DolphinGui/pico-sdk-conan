cmake_minimum_required(VERSION 3.15)
project(test_package C CXX)

find_package(raspberry_pi_pico_sdk REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)
# target_link_libraries(${PROJECT_NAME} ZLIB::ZLIB)
