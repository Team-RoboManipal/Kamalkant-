#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

#include <memory>

class Server : public rclcpp::Node{

    public:
    Server(): Node("server"){
        service=this->create_service<example_interfaces::srv::AddTwoInts>("AddTwoInts",
        std::bind(&Server::callback, this, std::placeholders::_1, std::placeholders::_2));
    }
    private:
    void callback(
    const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
    std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response){
        response->sum=request->a+request->b;
        RCLCPP_INFO(this->get_logger()," %lld + %lld = %lld",request->a,request->b,response->sum);
    }
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr service;
};


int main(int argc,char **argv){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Server>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;}