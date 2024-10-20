#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool compareLength(const string& a, const string& b) {
    return a.length() < b.length();
}

void sortCharacters(string& word) {
    sort(word.begin(), word.end());
}

int main() {
    vector<string> words;
    words.push_back("word");
    words.push_back("number");
    words.push_back("cat");

    sort(words.begin(), words.end(), compareLength);

    for (int i = 0; i < words.size(); i++) {
        cout << words[i] << endl;
    }

    for (int i = 0; i < words.size(); i++) {
        sortCharacters(words[i]);
        cout << words[i] << " ";
    }
    cout << endl;

    return 0;
}
