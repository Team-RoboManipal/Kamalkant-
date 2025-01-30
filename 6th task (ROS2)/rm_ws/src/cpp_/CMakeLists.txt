cmake_minimum_required(VERSION 3.10)
project(cpp_)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(example_interfaces REQUIRED)

#publisher
add_executable(pub src/pub.cpp)
ament_target_dependencies(pub rclcpp std_msgs)
install(TARGETS
  pub
  DESTINATION lib/${PROJECT_NAME})
#subscriber
add_executable(sub src/sub.cpp)
ament_target_dependencies(sub rclcpp std_msgs)
install(TARGETS
  sub
  DESTINATION lib/${PROJECT_NAME})
#server
add_executable(server src/server_.cpp)
ament_target_dependencies(server rclcpp example_interfaces)
install(TARGETS
  server
  DESTINATION lib/${PROJECT_NAME})

#client
add_executable(client src/client_.cpp)
ament_target_dependencies(client rclcpp example_interfaces)
install(TARGETS
  client
  DESTINATION lib/${PROJECT_NAME})



if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
