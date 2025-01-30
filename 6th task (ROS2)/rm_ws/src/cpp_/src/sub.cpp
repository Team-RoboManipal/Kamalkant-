#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <memory>
using namespace std::chrono_literals;

class Subscriber : public rclcpp::Node{
    public:
    Subscriber(): Node("Subscriber") {

        subscriber_=this->create_subscription<std_msgs::msg::String>("/topic1",10,std::bind(&Subscriber::callback,this,std::placeholders::_1));
    }
    private:
    void callback(const std_msgs::msg::String::SharedPtr msg){

        RCLCPP_INFO(this->get_logger(),"I heard:%s",msg->data.c_str());

    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_;
};



int main(int argc , char * argv[]){

    rclcpp::init(argc,argv);

    auto node=std::make_shared<Subscriber>();

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}


