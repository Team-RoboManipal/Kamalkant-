// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:srv/NSides.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__N_SIDES__STRUCT_HPP_
#define TUTORIAL_INTERFACES__SRV__DETAIL__N_SIDES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__srv__NSides_Request __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__srv__NSides_Request __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct NSides_Request_
{
  using Type = NSides_Request_<ContainerAllocator>;

  explicit NSides_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->n = 0ll;
    }
  }

  explicit NSides_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->n = 0ll;
    }
  }

  // field types and members
  using _n_type =
    int64_t;
  _n_type n;

  // setters for named parameter idiom
  Type & set__n(
    const int64_t & _arg)
  {
    this->n = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::srv::NSides_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::srv::NSides_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::srv::NSides_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::srv::NSides_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__srv__NSides_Request
    std::shared_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__srv__NSides_Request
    std::shared_ptr<tutorial_interfaces::srv::NSides_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NSides_Request_ & other) const
  {
    if (this->n != other.n) {
      return false;
    }
    return true;
  }
  bool operator!=(const NSides_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NSides_Request_

// alias to use template instance with default allocator
using NSides_Request =
  tutorial_interfaces::srv::NSides_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace tutorial_interfaces


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__srv__NSides_Response __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__srv__NSides_Response __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct NSides_Response_
{
  using Type = NSides_Response_<ContainerAllocator>;

  explicit NSides_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit NSides_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::srv::NSides_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::srv::NSides_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::srv::NSides_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::srv::NSides_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__srv__NSides_Response
    std::shared_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__srv__NSides_Response
    std::shared_ptr<tutorial_interfaces::srv::NSides_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NSides_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const NSides_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NSides_Response_

// alias to use template instance with default allocator
using NSides_Response =
  tutorial_interfaces::srv::NSides_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace tutorial_interfaces

namespace tutorial_interfaces
{

namespace srv
{

struct NSides
{
  using Request = tutorial_interfaces::srv::NSides_Request;
  using Response = tutorial_interfaces::srv::NSides_Response;
};

}  // namespace srv

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__N_SIDES__STRUCT_HPP_
