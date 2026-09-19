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
        int min = i;
        for(int j = i + 1; j < n; j++){
            if(data[j] < data[min]){
                min = j;
            }
        }
        int t = data[i];
        data[i] = data[min];
        data[min] = t;
    }

    cout << "Selection Sort: " << endl;
    for(int i = 0; i < n; i++){
        cout << data[i] << " ";
    }

    return 0;
}
