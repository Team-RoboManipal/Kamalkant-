#include <iostream>

void copyString(char *destination, const char *source) {
    while (*source != '\0') {
        *destination = *source;
        destination++;
        source++;
    }
    *destination = '\0'; 
}

int main() {
    char source[] = "Hello, world!";
    char destination[20];

    copyString(destination, source);

    std::cout << "Source string: " << source << std::endl;
    std::cout << "Destination string: " << destination << std::endl;

    return 0;
}
  