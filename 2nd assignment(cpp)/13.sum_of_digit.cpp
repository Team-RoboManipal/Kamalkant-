#include <iostream>

int main(){
    int inpu,output,temp;

    inpu=1234;
    output=0;

    while(inpu!=0){
        output+=inpu%10;
        inpu/=10;
    }
    std::cout<<output;
    return 0;

}