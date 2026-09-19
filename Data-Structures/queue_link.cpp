#include <iostream>
using namespace std;

struct Node{
    int data;
    Node* next;
};
Node* front = NULL;
Node* rear = NULL;
void enqueue(){
int x;
cout << "Enter 5 elements: ";
for (int i = 0; i < 5; ++i)
{
 cin >> x;
 Node* temp = new Node();
 temp->data = x;
 temp->next = NULL;
 if (rear == NULL){
 front = rear = temp;}
 else{
 rear->next = temp;
 rear = temp; }
    }
}
void dequeue(){
    if (front == NULL){
        cout << "Queue Underflow\n";
        return;
    }
    Node* temp = front;
    cout << "Deleted element: " << temp->data << endl;
    front = front->next;
    if (front == NULL)
        rear = NULL;
    delete temp;
}

void peek(){
    if (front == NULL){
        cout << "Queue is empty\n";
        return;
    }
    cout << "Front element: " << front->data << endl;
}
void display(){
    Node* temp = front;
    if (temp == NULL){
        cout << "Queue is empty\n";
        return;
    }
    cout << "Queue elements:\n";
    int count = 0;
    while (temp != NULL)
    {
        cout << temp->data << " ";
        ++count;
        if (count % 5 == 0)
            cout << endl;
        temp = temp->next;
    }

    if (count % 5 != 0)
        cout << endl;
}
int main(){
    int choice;
    do
    {
        cout << "\n1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1: enqueue(); break;
            case 2: dequeue(); break;
            case 3: peek(); break;
            case 4: display(); break;
        }
    } while (choice != 5);

    return 0;
}
