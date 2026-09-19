#include <iostream>
using namespace std;

int main() {
    int size, n, key;

    cout << "Enter size of hash table: ";
    cin >> size;

    int hash[size];

    for (int i = 0; i < size; i++)
        hash[i] = -1;

    cout << "Enter number of elements: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << "Enter key: ";
        cin >> key;

        int index = key % size;

        while (hash[index] != -1)
            index = (index + 1) % size;

        hash[index] = key;
    }

    cout << "\nHash Table:\n";
    for (int i = 0; i < size; i++) {
        cout << i << " --> ";
        if (hash[i] == -1)
            cout << "Empty";
        else
            cout << hash[i];
        cout << endl;
    }

    return 0;
}
