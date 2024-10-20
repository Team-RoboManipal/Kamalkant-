#include <iostream>
#include <iomanip> // for std::hex and std::oct
using namespace std;

int main() {
    int decimal;
    cout << "Enter a decimal number: ";
    cin >> decimal;
    cout << "Hexadecimal: " << hex << decimal << endl;
    cout << "Octal: " << oct << decimal << endl;

    // Output the number in binary
    cout << "Binary: ";
    for (int i = 31; i >= 0; i--) {
        cout << ((decimal >> i) & 1);
    }
    cout << endl;

    return 0;
}
