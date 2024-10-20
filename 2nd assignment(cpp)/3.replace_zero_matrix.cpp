#include <iostream>
using namespace std;
void printmat(int mat[3][3],int r, int c){
    cout<<"\n******************\n\n";
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cout<<mat[i][j]<<" ";      
        }
        cout<<"\n";

    }
    cout<<"\n******************\n ";
}
int main(){

    int input_matrix[3][3]={{1,2,0},{1,2,0},{1,2,3}};


    int r=sizeof(input_matrix)/sizeof(input_matrix[0]);
    int c=sizeof(input_matrix[0])/sizeof(input_matrix[0][0]);

    cout<<"inputted matrix:";

    printmat(input_matrix,r,c);
    //finding the target element(0)
    int rt,ct;
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if (input_matrix[i][j]==0){
                rt=i;
                ct=j;
                break;
            }
        }
    }
    cout<<"A"<<rt<<ct<<" is Zero \n";
    // setting the elements to 0
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if (i==rt||j==ct){
                input_matrix[i][j]=0;

            }
        }
    }
    cout<<"output matrix";
    printmat(input_matrix,r,c);

    return 0;
}