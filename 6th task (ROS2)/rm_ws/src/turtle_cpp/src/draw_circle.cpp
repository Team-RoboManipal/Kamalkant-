#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <cmath>

class DrawNode : public rclcpp::Node {
public:
    DrawNode() : Node("DrawCircle"), r(2.0) {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(100), std::bind(&DrawNode::draw_circle, this));
        start_time_ = this->now();
    }

private:
    void draw_circle() {
        rclcpp::Time current_time = this->now();
        double time_elapsed = (current_time - start_time_).seconds();
        
        if (time_elapsed < 2 * M_PI) {
            publish_msg(r, 0.0, 1.0);
        } else {
            publish_msg(0.0, 0.0, 0.0);
        }
    }

    void publish_msg(double x, double y, double z) {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = x;
        msg.linear.y = y;
        msg.angular.z = z;
        publisher_->publish(msg);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Time start_time_;
    double r;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<DrawNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
