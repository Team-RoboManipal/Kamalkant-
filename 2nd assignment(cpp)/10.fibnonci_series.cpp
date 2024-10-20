#include <iostream>

const int MAX_SIZE = 100;

int fibno(int n, int memo[]) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];
    memo[n] = fibno(n - 1, memo) + fibno(n - 2, memo);
    return memo[n];
}

void displayFibonacci(int count) {
    int memo[MAX_SIZE];
    for (int i = 0; i < MAX_SIZE; ++i) {
        memo[i] = -1;
    }
    for (int i = 0; i < count; ++i) {
        std::cout << fibno(i, memo) << " ";
    }
    std::cout << std::endl;
}

int main() {
    displayFibonacci(40);
    return 0;
}
