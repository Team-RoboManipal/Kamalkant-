#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <chrono>
#include <string>

using namespace std::chrono_literals;

class Publisher : public rclcpp::Node{
    public:
    Publisher(): Node("Publisher") , count_(0){

        publisher_ = this->create_publisher<std_msgs::msg::String>("/topic1",10);
        timer_=this->create_wall_timer(500ms,std::bind(&Publisher::callback,this));
    }
    void callback(){

        auto msg = std_msgs::msg::String();
        msg.data="Hello World:"+std::to_string(count_);
        RCLCPP_INFO(this->get_logger(),"Hello World : %zu",count_);
        publisher_->publish(msg);
        count_++;

    }
    private:
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_; //unsigned integer
};



int main(int argc , char * argv[]){

    rclcpp::init(argc,argv);

    auto node=std::make_shared<Publisher>();

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}


