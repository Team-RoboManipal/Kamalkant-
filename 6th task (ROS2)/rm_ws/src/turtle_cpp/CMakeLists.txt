cmake_minimum_required(VERSION 3.8)
project(turtle_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(turtlesim REQUIRED)

#goal
add_executable(goal src/goal.cpp)
ament_target_dependencies(goal rclcpp geometry_msgs turtlesim)
install(TARGETS
  goal
  DESTINATION lib/${PROJECT_NAME})
#polygon
add_executable(polygon src/polygon.cpp)
ament_target_dependencies(polygon rclcpp geometry_msgs)
install(TARGETS
  polygon
  DESTINATION lib/${PROJECT_NAME})
#controller
add_executable(controller src/controller.cpp)
ament_target_dependencies(controller rclcpp geometry_msgs)
install(TARGETS
  controller
  DESTINATION lib/${PROJECT_NAME})
#D
add_executable(d src/d_.cpp)
ament_target_dependencies(d rclcpp geometry_msgs)
install(TARGETS
  d
  DESTINATION lib/${PROJECT_NAME})
#draw_circle
add_executable(draw_circle src/draw_circle.cpp)
ament_target_dependencies(draw_circle rclcpp geometry_msgs)
install(TARGETS
  draw_circle
  DESTINATION lib/${PROJECT_NAME})
  

ament_package()
