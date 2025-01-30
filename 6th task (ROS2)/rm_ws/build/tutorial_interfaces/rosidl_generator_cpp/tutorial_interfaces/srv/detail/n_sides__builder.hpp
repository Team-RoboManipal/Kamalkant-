// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:srv/NSides.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__N_SIDES__BUILDER_HPP_
#define TUTORIAL_INTERFACES__SRV__DETAIL__N_SIDES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/srv/detail/n_sides__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_NSides_Request_n
{
public:
  Init_NSides_Request_n()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::tutorial_interfaces::srv::NSides_Request n(::tutorial_interfaces::srv::NSides_Request::_n_type arg)
  {
    msg_.n = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::NSides_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::NSides_Request>()
{
  return tutorial_interfaces::srv::builder::Init_NSides_Request_n();
}

}  // namespace tutorial_interfaces


namespace tutorial_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::NSides_Response>()
{
  return ::tutorial_interfaces::srv::NSides_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__N_SIDES__BUILDER_HPP_
