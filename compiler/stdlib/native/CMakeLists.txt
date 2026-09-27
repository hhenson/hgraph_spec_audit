cmake_minimum_required(VERSION 3.26)
project(hgraph_stdlib_conformance LANGUAGES CXX)
find_package(hgraph CONFIG REQUIRED)
find_package(Python REQUIRED COMPONENTS Interpreter)
include("${hgraph_DIR}/../hgl/HglLanguage.cmake")
set(corpus "${CMAKE_CURRENT_SOURCE_DIR}/..")
hgl_add_module(conformance_stdlib STATIC HGL "${corpus}/nodes.hgl"
    LINK_LIBRARIES hgl::standard_library)
add_custom_command(OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/cases.inc"
    COMMAND "${Python_EXECUTABLE}" "${CMAKE_CURRENT_SOURCE_DIR}/../../../tools/stdlib_cases.py"
        --cases "${corpus}/cases.json" --output "${CMAKE_CURRENT_BINARY_DIR}/cases.inc"
    DEPENDS "${corpus}/cases.json" "${CMAKE_CURRENT_SOURCE_DIR}/../../../tools/stdlib_cases.py"
    VERBATIM)
add_executable(stdlib_conformance main.cpp "${CMAKE_CURRENT_BINARY_DIR}/cases.inc")
target_include_directories(stdlib_conformance PRIVATE "${CMAKE_CURRENT_BINARY_DIR}")
target_link_libraries(stdlib_conformance PRIVATE conformance_stdlib)
if(COMMAND hgraph_link_python_embedding)
    hgraph_link_python_embedding(stdlib_conformance)
endif()
enable_testing()
add_test(NAME stdlib_conformance COMMAND stdlib_conformance)
