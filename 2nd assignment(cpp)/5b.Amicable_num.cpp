#include <iostream>

using namespace std;

int sum_of_divisors(int num) {
    int sum = 0;
    for (int i = 1; i <= num / 2; ++i) {
        if (num % i == 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    int num1, num2;
    
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    
    int sum1 = sum_of_divisors(num1);
    int sum2 = sum_of_divisors(num2);
    
    if (sum1 == num2 && sum2 == num1) {
        cout << num1 << " and " << num2 << " are Amicable numbers." << endl;
    } else {
        cout << num1 << " and " << num2 << " are not Amicable numbers." << endl;
    }
    
    return 0;
}
