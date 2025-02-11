# Install script for directory: /Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/geometry_tutorials/geometry_tutorials

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/install/geometry_tutorials")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/geometry_tutorials")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/geometry_tutorials")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials/environment" TYPE FILE FILES "/Users/kamal/miniconda3/envs/ros_hum/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials/environment" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials/environment" TYPE FILE FILES "/Users/kamal/miniconda3/envs/ros_hum/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials/environment" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_index/share/ament_index/resource_index/packages/geometry_tutorials")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials/cmake" TYPE FILE FILES
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_core/geometry_tutorialsConfig.cmake"
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/ament_cmake_core/geometry_tutorialsConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/geometry_tutorials" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/geometry_tutorials/geometry_tutorials/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/geometry_tutorials/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
