#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <iostream>
#include <string>
#include <thread>
class NodeB : public rclcpp::Node {
    public:
    NodeB():Node("NodeB"){
        publisher_=this->create_publisher<std_msgs::msg::String>("/b2a",10);
        subscriber_ = this->create_subscription<std_msgs::msg::String>("/a2b", 10, [this](std::shared_ptr<const std_msgs::msg::String> msg) {callback(msg);});

        RCLCPP_INFO(this->get_logger(),"Node B is Started");
        input_thread_ = std::thread(&NodeB::getinput, this);

    }
    ~NodeB() {
    if (input_thread_.joinable()) {
        input_thread_.join();  
    }
    }
    private:
    void callback(std::shared_ptr<const std_msgs::msg::String> msg){
        std::cout<<"A:"<<msg->data.c_str()<<std::endl;
    }
    void getinput(){
        while(rclcpp::ok()){
            std::string user_input;
            //std::cout<<"B:";
            std::getline(std::cin,user_input);
            if (user_input.empty()) {
                continue; 
            }
            this->current_input.data=user_input;
            publisher_->publish(current_input);
        }
        

    }

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber_;
    std_msgs::msg::String current_input;
    std::thread input_thread_;

};

int main(int argc,char * argv[]){
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<NodeB>());
    rclcpp::shutdown();
    return 0;
}