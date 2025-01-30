#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <cmath>

class Polygon : public rclcpp::Node {
public:
    Polygon() : Node("Draw_polygon") {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        RCLCPP_INFO(this->get_logger(), "Polygon node has been started");
    }

    void draw_polygon(int n, double side_length) {
        double exterior_angle = (2 * M_PI) / n;
        RCLCPP_INFO(this->get_logger(), "Drawing polygon with %d sides, each of length %.2f", n, side_length);

        for (int i = 0; i < n; i++) {
            RCLCPP_INFO(this->get_logger(), "Drawing side %d", i + 1);
            for (int j = 0; j < static_cast<int>(side_length); j++) {
                publish_twist(1.0, 0.0, 0.0); // Move forward
                RCLCPP_INFO(this->get_logger(), "Moving forward step %d", j + 1);
                rclcpp::sleep_for(std::chrono::seconds(1));
            }
            publish_twist(0.0, 0.0, exterior_angle); // Rotate
            RCLCPP_INFO(this->get_logger(), "Rotating by %.2f radians", exterior_angle);
            rclcpp::sleep_for(std::chrono::seconds(2));
        }
    }

private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;

    void publish_twist(double x, double y, double z) {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = x;
        msg.linear.y = y;
        msg.angular.z = z;
        publisher_->publish(msg);
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Polygon>();
    node->draw_polygon(6, 1.0);
    rclcpp::shutdown();
    return 0;
}
