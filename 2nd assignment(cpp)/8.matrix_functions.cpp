#include <iostream>
using namespace std;

void multiplyMatrices(int A[][3], int B[][3], int C[][3], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

void transposeMatrix(int A[][3], int T[][3], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            T[i][j] = A[j][i];
        }
    }
}

void printMatrix(int A[][3], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    const int n = 3;
    int A[n][n] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[n][n] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int AB[n][n], AB_T[n][n], A_T[n][n], B_T[n][n], BT_AT[n][n];

    multiplyMatrices(A, B, AB, n);
    transposeMatrix(AB, AB_T, n);
    transposeMatrix(A, A_T, n);
    transposeMatrix(B, B_T, n);
    multiplyMatrices(B_T, A_T, BT_AT, n);

    bool identityVerified = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (AB_T[i][j] != BT_AT[i][j]) {
                identityVerified = false;
                break;
            }
        }
    }

    cout << "Matrix AB (A * B):\n";
    printMatrix(AB, n);
    cout << "Transpose of AB ((A * B)'):\n";
    printMatrix(AB_T, n);
    cout << "Transpose of A (A'):\n";
    printMatrix(A_T, n);
    cout << "Transpose of B (B'):\n";
    printMatrix(B_T, n);
    cout << "Matrix B' * A' (B' * A'):\n";
    printMatrix(BT_AT, n);

    if (identityVerified) {
        cout << "The identity (A * B)' = B' * A' is verified!" << endl;
    } else {
        cout << "The identity (A * B)' = B' * A' is not verified." << endl;
    }

    return 0;
}
