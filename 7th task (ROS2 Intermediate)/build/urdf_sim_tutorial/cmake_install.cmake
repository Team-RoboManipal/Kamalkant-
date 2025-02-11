# Install script for directory: /Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/urdf_sim_tutorial

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/install/urdf_sim_tutorial")
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

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/Users/kamal/miniconda3/envs/ros_hum/bin/llvm-objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE DIRECTORY FILES
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/urdf_sim_tutorial/config"
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/urdf_sim_tutorial/launch"
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/urdf_sim_tutorial/rviz"
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/urdf_sim_tutorial/urdf"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/urdf_sim_tutorial")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/urdf_sim_tutorial")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial/environment" TYPE FILE FILES "/Users/kamal/miniconda3/envs/ros_hum/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial/environment" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial/environment" TYPE FILE FILES "/Users/kamal/miniconda3/envs/ros_hum/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial/environment" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_index/share/ament_index/resource_index/packages/urdf_sim_tutorial")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial/cmake" TYPE FILE FILES
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_core/urdf_sim_tutorialConfig.cmake"
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/ament_cmake_core/urdf_sim_tutorialConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/urdf_sim_tutorial" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/urdf_sim_tutorial/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/urdf_sim_tutorial/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
