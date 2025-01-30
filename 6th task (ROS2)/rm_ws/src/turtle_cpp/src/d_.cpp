#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <cmath>

class DrawNode : public rclcpp::Node {
public:
    DrawNode() : Node("DrawCircle"), state("semicircle"), r(2), line_length(4) {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(100), std::bind(&DrawNode::draw_d, this));
        start_time = this->now();
    }

private:
    void draw_d() {
        auto current_time = this->now();
        double time_elapsed = (current_time - start_time).seconds();
        
        if (state == "semicircle") {
            if (time_elapsed < M_PI) { // Time for a half-circle (180 degrees)
                msg(r, 0, 1);
            } else {
                state = "turn";
                start_time = this->now();
                msg(0, 0, 0);
            }
        } else if (state == "turn") {
            if (time_elapsed < (M_PI / 2) + 0.11) { // Rotate for 90 degrees
                msg(0, 0, 1);
            } else {
                state = "line";
                start_time = this->now();
                msg(0, 0, 0);
            }
        } else if (state == "line") {
            if (time_elapsed < line_length / r) { // Move straight for the line length
                msg(r, 0, 0);
            } else {
                state = "done";
                msg(0, 0, 0);
            }
        }
    }

    void msg(double x, double y, double z) {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = x;
        msg.linear.y = y;
        msg.angular.z = z;
        publisher_->publish(msg);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Time start_time;
    std::string state;
    double r;
    double line_length;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<DrawNode>());
    rclcpp::shutdown();
    return 0;
}
