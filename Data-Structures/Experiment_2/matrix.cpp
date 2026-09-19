#include<iostream>
using namespace std;

int main() {
    int a[10][10], b[10][10], c[10][10];
    int i, j, n, d;

    cout << "Enter the order of matrix: ";
    cin >> n;

    cout << "Enter the elements of matrix 1:\n";
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            cin >> a[i][j];
        }
    }

    cout << "Enter the elements of matrix 2:\n";
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            cin >> b[i][j];
        }
    }

    cout << "1. Add  2. Subtract\n";
    cin >> d;

    if(d == 1) {
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                c[i][j] = a[i][j] + b[i][j];
            }
        }
    } else {
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                c[i][j] = a[i][j] - b[i][j];
            }
        }
    } 

    cout << "Resultant Matrix:\n";
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            cout << c[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}

