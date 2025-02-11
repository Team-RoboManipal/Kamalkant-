# Install script for directory: /Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/geometry_tutorials/turtle_tf2_cpp

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/install/turtle_tf2_cpp")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp" TYPE EXECUTABLE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/static_turtle_tf2_broadcaster")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/static_turtle_tf2_broadcaster" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/static_turtle_tf2_broadcaster")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Users/kamal/miniconda3/envs/ros_hum/bin/arm64-apple-darwin20.0.0-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/static_turtle_tf2_broadcaster")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/CMakeFiles/static_turtle_tf2_broadcaster.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp" TYPE EXECUTABLE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/turtle_tf2_broadcaster")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_broadcaster" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_broadcaster")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Users/kamal/miniconda3/envs/ros_hum/bin/arm64-apple-darwin20.0.0-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_broadcaster")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/CMakeFiles/turtle_tf2_broadcaster.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp" TYPE EXECUTABLE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/turtle_tf2_listener")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_listener" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_listener")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Users/kamal/miniconda3/envs/ros_hum/bin/arm64-apple-darwin20.0.0-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_listener")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/CMakeFiles/turtle_tf2_listener.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp" TYPE EXECUTABLE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/fixed_frame_tf2_broadcaster")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/fixed_frame_tf2_broadcaster" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/fixed_frame_tf2_broadcaster")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Users/kamal/miniconda3/envs/ros_hum/bin/arm64-apple-darwin20.0.0-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/fixed_frame_tf2_broadcaster")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/CMakeFiles/fixed_frame_tf2_broadcaster.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp" TYPE EXECUTABLE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/dynamic_frame_tf2_broadcaster")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/dynamic_frame_tf2_broadcaster" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/dynamic_frame_tf2_broadcaster")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Users/kamal/miniconda3/envs/ros_hum/bin/arm64-apple-darwin20.0.0-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/dynamic_frame_tf2_broadcaster")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/CMakeFiles/dynamic_frame_tf2_broadcaster.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp" TYPE EXECUTABLE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/turtle_tf2_message_filter")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_message_filter" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_message_filter")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/Users/kamal/miniconda3/envs/ros_hum/bin/arm64-apple-darwin20.0.0-strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtle_tf2_cpp/turtle_tf2_message_filter")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/CMakeFiles/turtle_tf2_message_filter.dir/install-cxx-module-bmi-noconfig.cmake" OPTIONAL)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE DIRECTORY FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/geometry_tutorials/turtle_tf2_cpp/launch")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/turtle_tf2_cpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/turtle_tf2_cpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp/environment" TYPE FILE FILES "/Users/kamal/miniconda3/envs/ros_hum/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp/environment" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp/environment" TYPE FILE FILES "/Users/kamal/miniconda3/envs/ros_hum/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp/environment" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/path.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/local_setup.bash")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/local_setup.sh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_environment_hooks/package.dsv")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_index/share/ament_index/resource_index/packages/turtle_tf2_cpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp/cmake" TYPE FILE FILES
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_core/turtle_tf2_cppConfig.cmake"
    "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/ament_cmake_core/turtle_tf2_cppConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtle_tf2_cpp" TYPE FILE FILES "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/src/geometry_tutorials/turtle_tf2_cpp/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/kamal/git_/Kamalkant-/7th task (ROS2 Intermediate)/build/turtle_tf2_cpp/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
