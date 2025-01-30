# Package Executables Overview

This repository contains various ROS2 packages and their respective executables.

## Packages and Executables

| **Package**            | **Executables**                           |
|------------------------|-----------------------------------------|
| `chat`                | `a`, `b`                                 |
| `cpp_`                | `pub_sub`, `server`, `client`           |
| `py_examples`         | `pub_sub`, `server`, `client`           |
| `turtle_cpp`          | `goal_polygon_controller_d`, `draw_circle` |
| `turtle_sim`          | `goal_polygon_controller_d`, `draw_circle` |
| `polygon_turtle`      | `poly`                                  |
| `tutorial_interface`  | `tutorial_interfaces/srv/NSides`       |
| `polygon_cpp`         | `Poly`                                  |

## Description

- **chat**: Contains two executables (`a` and `b`).
- **cpp_**: Implements publisher-subscriber and client-server communication in C++.
- **py_examples**: Similar to `cpp_`, but implemented in Python.
- **turtle_cpp** and **turtle_sim**: Provide functionalities for controlling a polygon-based turtle simulation.
- **polygon_turtle**: Offers a `poly` executable, likely for polygon drawing.
- **tutorial_interface**: Contains a service (`NSides`) under `tutorial_interfaces/srv/`.
- **polygon_cpp**: Provides the `Poly` executable.
