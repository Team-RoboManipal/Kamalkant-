#include <iostream>
#include <string>
using namespace std;
bool hillnumber(string& x){
    int n= x.length();

    if (n<3){
        return false;
    }
    int i = 0;

    while(i<n-1 && x[i]<x[i+1]){
        i++;
    }
    if (i==0||i==n-1){
        return false;
    }
    if(i<n-1&& x[i]>x[i+1]){
        i++;
    }

    return i==n-1;


}


int main() {
    string num;
    
    // Input the number
    cout << "Enter a number: ";
    cin >> num;
    
    // Check if it's a hill number and display result
    if (hillnumber(num)) {
        cout << num << " is a Hill Number." << endl;
    } else {
        cout << num << " is not a Hill Number." << endl;
    }

    return 0;
}
