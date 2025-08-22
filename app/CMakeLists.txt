# cmake_minimum_required(VERSION 3.20)

add_executable(hello
  "helloworld.cpp"
  "sample.cpp"
)

target_include_directories(hello
  PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/
)

# target_link_directories(hello

# )

# install files
# install(TARGETS
#     hello
#     DESTINATION "${CMAKE_INSTALL_PREFIX}"
# )

# Find all .su files in the build directory
file(GLOB SU_FILES LIST_DIRECTORIES false
  "${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/hello.dir/*.su"
)

install(FILES ${SU_FILES}
  DESTINATION "${CMAKE_INSTALL_PREFIX}/su"
)

# Find all .su files in the build directory
file(GLOB GRAPH_FILES LIST_DIRECTORIES false
  "${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/hello.dir/*.local*1"
)

install(FILES ${GRAPH_FILES}
  DESTINATION "${CMAKE_INSTALL_PREFIX}/graph"
)
