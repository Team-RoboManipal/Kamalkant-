#include <iostream>

void sort(char ar[],int len){
    char temp;
    for (int i =0;i<len-1;i++){

        for (int j =0;j<len-1-i;j++){

            if (ar[j+1]< ar[j]){

                temp=ar[j];
                ar[j]=ar[j+1];
                ar[j+1]=temp;


            }
        }   
    }
    std::cout<<ar;
}

int main(){

    char ar[]="worksheet";
    int len = sizeof(ar)/sizeof(ar[0])-1;
    sort(ar,len);
    return 0;
}