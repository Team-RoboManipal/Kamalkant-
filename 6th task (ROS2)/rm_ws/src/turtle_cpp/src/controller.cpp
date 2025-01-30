#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <termios.h>
#include <unistd.h>
#include <iostream>

class ControllerNode : public rclcpp::Node
{
public:
    ControllerNode() : Node("controller_node")
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        print_instructions();
        timer_ = this->create_wall_timer(std::chrono::milliseconds(100), std::bind(&ControllerNode::check_key, this));
    }

private:
    void check_key()
    {
        char key = get_key();
        if (key != '\0') // Key pressed
        {
            redirect(key);
        }
    }

    void redirect(char key)
    {
        if (key == 'w') {
            send_msg(1.0, 0.0, 0.0); // Move forward
        } else if (key == 's') {
            send_msg(-1.0, 0.0, 0.0); // Move backward
        } else if (key == 'a') {
            send_msg(0.0, 0.0, 1.0); // Rotate counterclockwise
        } else if (key == 'd') {
            send_msg(0.0, 0.0, -1.0); // Rotate clockwise
        } else if (key == 'q') {
            RCLCPP_INFO(this->get_logger(), "Exiting...");
            rclcpp::shutdown();
        }
    }

    void send_msg(double linear_x, double linear_y, double angular_z)
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = linear_x;
        msg.linear.y = linear_y;
        msg.angular.z = angular_z;
        publisher_->publish(msg);
    }

    char get_key()
    {
        struct termios oldt, newt;
        char ch = '\0';
        tcgetattr(STDIN_FILENO, &oldt);
        newt = oldt;
        newt.c_lflag &= ~ICANON;  // Disable buffering
        newt.c_lflag &= ~ECHO;    // Disable echo
        tcsetattr(STDIN_FILENO, TCSANOW, &newt);
        ch = getchar();
        tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
        return ch;
    }

    void print_instructions()
    {
        std::string instructions = R"(
        Welcome to Turtle Controller!

        Use the following keys to control the turtle:
        - 'w' : Move forward
        - 's' : Move backward
        - 'a' : Rotate counterclockwise
        - 'd' : Rotate clockwise
        - 'q' : Quit the program

        Press any of the above keys to start controlling the turtle.
        )";
        RCLCPP_INFO(this->get_logger(), instructions.c_str());
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<ControllerNode>());
    rclcpp::shutdown();
    return 0;
}
