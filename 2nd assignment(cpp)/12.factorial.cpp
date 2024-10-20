#include <iostream>

int factorial(int n) {
    
    if (n <= 1) {
        return 1;
    }

    return n * factorial(n - 1);
}

int main() {
    int a = 10;
    
    // Since 40! exceeds long long range, this will still overflow.
    int result = factorial(a);

    std::cout << "Factorial: " << result << std::endl;
    
    return 0;
}
