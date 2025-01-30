#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "turtlesim/msg/pose.hpp"
#include <cmath>
#include <cstdlib>

class GoalNode : public rclcpp::Node {
public:
    GoalNode(float goal_x, float goal_y)
        : Node("goal_node"), goal_x_(goal_x), goal_y_(goal_y), reached_goal_(false) {
        
        tolerance_ = 1.5;
        linear_constant_ = 1.5;
        angular_constant_ = 6.0;
        
        RCLCPP_INFO(this->get_logger(), "Going to goal: X=%f, Y=%f", goal_x_, goal_y_);
        
        subscriber_ = this->create_subscription<turtlesim::msg::Pose>(
            "/turtle1/pose", 10, std::bind(&GoalNode::pose_callback, this, std::placeholders::_1));
        
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
    }

private:
    float goal_x_, goal_y_;
    float tolerance_;
    float linear_constant_;
    float angular_constant_;
    bool reached_goal_;

    rclcpp::Subscription<turtlesim::msg::Pose>::SharedPtr subscriber_;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;

    void pose_callback(const turtlesim::msg::Pose::SharedPtr pose) {
        if (!reached_goal_) {
            if (distance(pose) <= tolerance_) {
                reached_goal_ = true;
                RCLCPP_INFO(this->get_logger(), "Goal reached!");
            } else {
                publish_velocity(linear_velocity(pose), 0.0, angular_velocity(pose));
            }
        }
    }

    float distance(const turtlesim::msg::Pose::SharedPtr pose) {
        return std::sqrt(std::pow(pose->x - goal_x_, 2) + std::pow(pose->y - goal_y_, 2));
    }

    float linear_velocity(const turtlesim::msg::Pose::SharedPtr pose) {
        return linear_constant_ * distance(pose);
    }

    float angular_velocity(const turtlesim::msg::Pose::SharedPtr pose) {
        float angle_to_goal = std::atan2(goal_y_ - pose->y, goal_x_ - pose->x);
        float angle_diff = angle_to_goal - pose->theta;
        return angular_constant_ * angle_diff;
    }

    void publish_velocity(float x, float y, float z) {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = x;
        msg.linear.y = y;
        msg.angular.z = z;
        publisher_->publish(msg);
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    
    if (argc != 3) {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "Usage: ros2 run <pkg_name> goal X Y");
        return 1;
    }
    
    float goal_x = std::stof(argv[1]);
    float goal_y = std::stof(argv[2]);
    
    auto node = std::make_shared<GoalNode>(goal_x, goal_y);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
