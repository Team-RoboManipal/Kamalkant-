# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_chat_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED chat_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(chat_FOUND FALSE)
  elseif(NOT chat_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(chat_FOUND FALSE)
  endif()
  return()
endif()
set(_chat_CONFIG_INCLUDED TRUE)

# output package information
if(NOT chat_FIND_QUIETLY)
  message(STATUS "Found chat: 0.0.0 (${chat_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'chat' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${chat_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(chat_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${chat_DIR}/${_extra}")
endforeach()
