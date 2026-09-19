#include <iostream>
using namespace std;
#define SIZE 100
int queueArr[SIZE];
int front = -1;
int rear = -1;
void enqueue() {
    int x;
    cout << "Enter 5 elements: ";
    for (int i = 0; i < 5; i++) {
        cin >> x;
        if (rear == SIZE - 1) {
            cout << "Queue Overflow\n";
            return;
        }
        if (front == -1) 
            front = 0;
        queueArr[++rear] = x;
    }
}
void dequeue() {
    if (front == -1 || front > rear) {
        cout << "Queue Underflow\n";
        return;
    }
    cout << "Deleted element: " << queueArr[front++] << endl;
    if (front > rear)
        front = rear = -1;
}
void peek() {
    if (front == -1 || front > rear) {
        cout << "Queue is empty\n";
        return;
    }
    cout << "Front element: " << queueArr[front] << endl;
}
void display() {
    if (front == -1 || front > rear) {
        cout << "Queue is empty\n";
        return;
    }
    cout << "Queue elements:\n";
    for (int i = front; i <= rear; i++) {
        cout << queueArr[i] << " ";
    }
    cout << endl;
}
int main() {
int choice;
do {
    cout << "\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit\n";
    cout << "Enter your choice: ";
    cin >> choice;
    switch (choice) {
    case 1: enqueue(); break;
    case 2: dequeue(); break;
    case 3: peek(); break;
    case 4: display(); break;
 }
    } while (choice != 5);
    return 0;
}
