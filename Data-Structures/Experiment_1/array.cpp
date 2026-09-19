#include <iostream>
using namespace std;

int main() {
    int arr[10] = {10, 20, 30, 40, 50};
    int n = 5;
    int i;

    // 1. Traversal
    cout << "Array elements: ";
    for (i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // 2. Insertion
    int p = 2;
    int value = 25;
    for (i = n; i > p; i--) {
        arr[i] = arr[i - 1];
    }
    arr[p] = value;
    n++;

    cout << "After insertion: ";
    for (i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // 3. Deletion
    p = 3;
    for (i = p; i < n - 1; i++) {
        arr[i] = arr[i + 1];
    }
    n--;

    cout << "After deletion: ";
    for (i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // 4. Searching 
    int a = 40;
    for (i = 0; i < n; i++) {
        if (arr[i] == a) {
            cout << "Element " << a << " found at index " << i << endl;
        
        }
    }

    // 5. Updation 
    arr[1] = 100;

    cout << "After updation: ";
    for (i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
