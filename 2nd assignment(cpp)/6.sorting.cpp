#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    
    while (low <= high) {
        int mid = (low + high) / 2;
        
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }
    
    return -1;
}

int main() {
    int n, choice;
    char method;
    
    cout << "Enter the number of elements in the array: ";
    cin >> n;
    
    int arr[n];
    
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    cout << "Enter 's' for Selection Sort or 'b' for Bubble Sort: ";
    cin >> method;
    
    if (method == 's') {
        selectionSort(arr, n);
        cout << "Array sorted using Selection Sort." << endl;
    } else if (method == 'b') {
        bubbleSort(arr, n);
        cout << "Array sorted using Bubble Sort." << endl;
    } else {
        cout << "Invalid choice!" << endl;
        return 1;
    }
    
    cout << "Sorted Array: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    int key;
    cout << "Enter the element to search for: ";
    cin >> key;
    
    int position = binarySearch(arr, n, key);
    
    if (position != -1)
        cout << "Element found at position: " << position + 1 << endl;
    else
        cout << "Element not found in the array." << endl;
    
    return 0;
}
