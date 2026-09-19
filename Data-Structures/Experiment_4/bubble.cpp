#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "Enter no. of elements: " << endl;
    cin >> n;

    int data[n];
    cout<<"Enter elements: "<<endl;
    for(int i = 0; i < n; i++){
        cin >> data[i];
    }

    for(int i = 0; i < n - 1; i++){
        for(int j = 0; j < n - 1 - i; j++){
            if(data[j] > data[j + 1]){
                int t = data[j];
                data[j] = data[j + 1];
                data[j + 1] = t;
            }
        }
    }
    cout << "Bubble Sort: " << endl;
    for(int i = 0; i < n; i++){
        cout << data[i] << " ";
    }
    return 0;
}

