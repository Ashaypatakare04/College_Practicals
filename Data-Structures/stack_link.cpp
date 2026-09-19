#include <iostream>
using namespace std;
struct Node {
    int data;
    Node* next;
};
Node* top = NULL;
void push() {
    int x;
    cout << "Enter element: ";
    cin >> x;
    Node* temp = new Node();
    temp->data = x;
    temp->next = top;
    top = temp;
}
void pop() {
    if (top == NULL) {
        cout << "Stack Underflow\n";
        return;
    }
    Node* temp = top;
    cout << "Deleted element: " << temp->data << endl;
    top = top->next;
    delete temp;
}
void peek() {
    if (top == NULL) {
        cout << "Stack is empty\n";
        return;
    }
    cout << "Top element: " << top->data << endl;
}
void display() {
    if (top == NULL) {
        cout << "Stack is empty\n";
        return;
    }
    Node* temp = top;
    cout << "Stack elements:\n";

    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}
int main() {
    int choice;
    do {
        cout << "\n1.Push\n2.Pop\n3.Peek\n4.Display\n5.Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice) {
            case 1: push(); break;
            case 2: pop(); break;
            case 3: peek(); break;
            case 4: display(); break;
        }
    } while (choice != 5);
    return 0;
}
