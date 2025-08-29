cmake_minimum_required(VERSION 3.20)

project(StackSize_Project VERSION 1.0.0 LANGUAGES CXX C)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fstack-usage")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fdump-tree-local-fnsummary")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fdump-ipa-cgraph")

add_subdirectory(app)