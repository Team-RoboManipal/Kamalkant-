#include <iostream>
using namespace std;

int a[10][10],b[10][10],r[10][10];
//function to get matrix input
void printmat(int mat[10][10],int r, int c){
    cout<<"\n******************\n\n";
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cout<<mat[i][j]<<" ";      
        }
        cout<<"\n";

    }
    cout<<"\n******************\n ";



}
void matrixinput(int mat[10][10],string name,int r, int c){

    cout<<name<<"\n";

    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<"ENTER VALUE FOR A"<<i<<j<<":";
            cin>>mat[i][j];        
        }
    }

    cout<<"INPUTTED MATRIX:";

    printmat(mat,r,c);

}



int main(){
    //getting data about matrix
    int c1,c2,r1,r2;

    cout <<"MATRIX MULTIPLICATION \n";
    cout <<"MATRIX 1 \n";
    cout <<"ENTER NUMBER OF ROW   :";
    cin >> r1;
    cout <<"ENTER NUMBER OF COLUMN:";
    cin >> c1;
    cout <<"MATRIX 2 \n";
    cout <<"ENTER NUMBER OF ROW   :";
    cin >> r2;
    cout <<"ENTER NUMBER OF COLUMN:";
    cin >> c2;

    while(c1!=r2){
        cout <<"Error! column of first matrix not equal to row of second. \n";
        cout <<"MATRIX 1 \n";
        cout <<"ENTER NUMBER OF ROW   :";
        cin >> r1;
        cout <<"ENTER NUMBER OF COLUMN:";
        cin >> c1;
        cout <<"MATRIX 2 \n";
        cout <<"ENTER NUMBER OF ROW   :";
        cin >> r2;
        cout <<"ENTER NUMBER OF COLUMN:";
        cin >> c2;

    }

    cout <<"Great you entered a valid matrix !! \n";
    

    //assigning to a matrix
    matrixinput(a,"First matrix",r1,c1);
    matrixinput(b,"Second Matrix",r2,c2);

    //zero matrix

    for(int i=0;i<r1;i++){
        for(int j=0;j<c2;j++){
            r[i][j]=0;        
        }
    }

    //multiplication part
    for(int i=0;i<r1;i++){
        for(int j=0;j<c2;j++){
            r[i][j] = 0;
            for(int k =0;k<c1;k++){
                r[i][j]+=a[i][k]*b[k][j]; 
            }
                   
        }
    }

    cout<<"answer:";

    printmat(r,r1,c2);

    return 0;
}