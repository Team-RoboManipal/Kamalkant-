#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "tutorial_interfaces/srv/n_sides.hpp"
#include <cmath>

class PolygonNode : public rclcpp::Node {
public:
    PolygonNode() : Node("Draw_polygon") {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        server_ = this->create_service<tutorial_interfaces::srv::NSides>("Polygon",
                     std::bind(&PolygonNode::callback, this, std::placeholders::_1, std::placeholders::_2));
        RCLCPP_INFO(this->get_logger(), "Polygon node has been started");
    }

private:
    void callback(const std::shared_ptr<tutorial_interfaces::srv::NSides::Request> request,
                  std::shared_ptr<tutorial_interfaces::srv::NSides::Response> response) {
        (void)response; 
        int n = request->n;
        draw_polygon(n, 2);
    }

    void draw_polygon(int n, double side_length) {
        double exterior_angle = M_PI * 2 / n;
        RCLCPP_INFO(this->get_logger(), "Drawing polygon with %d sides, each of length %.2f", n, side_length);

        for (int i = 0; i < n; i++) {
            RCLCPP_INFO(this->get_logger(), "Drawing side %d", i + 1);
            for (int j = 0; j < static_cast<int>(side_length); j++) {
                msg(1.0, 0.0, 0.0); // Move forward
                RCLCPP_INFO(this->get_logger(), "Moving forward step %d", j + 1);
                rclcpp::sleep_for(std::chrono::seconds(1));
            }
            msg(0.0, 0.0, exterior_angle); // Rotate
            RCLCPP_INFO(this->get_logger(), "Rotating by %.2f radians", exterior_angle);
            rclcpp::sleep_for(std::chrono::seconds(1));
        }
    }

    void msg(double x, double y, double z) {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = x;
        msg.linear.y = y;
        msg.angular.z = z;
        publisher_->publish(msg);
        RCLCPP_INFO(this->get_logger(), "Published message: linear.x=%.2f, linear.y=%.2f, angular.z=%.2f", x, y, z);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::Service<tutorial_interfaces::srv::NSides>::SharedPtr server_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PolygonNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
