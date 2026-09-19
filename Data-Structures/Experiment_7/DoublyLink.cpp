#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node *prev, *next;
};
struct Node* head = NULL;
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->prev = newNode->next = NULL;
    return newNode;
}
void insertBeginning(int data) {
    struct Node* newNode = createNode(data);
    if (head != NULL) {
    head->prev = newNode;
    newNode->next = head;
}
    head = newNode;
}
void insertEnd(int data) {
    struct Node* newNode = createNode(data);
    if (head == NULL) {
    head = newNode;
    return;
}
    struct Node* temp = head;
    while (temp->next != NULL)
    temp = temp->next;
    temp->next = newNode;
    newNode->prev = temp;
}
void insertAtPosition(int data, int pos) {
    if (pos == 1) {
    insertBeginning(data);
    return;
}
    struct Node* newNode = createNode(data);
    struct Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++)
    temp = temp->next;
    if (temp == NULL) {
    printf("Invalid position\n");
    return;
}
    newNode->next = temp->next;
    newNode->prev = temp;
    if (temp->next != NULL)
    temp->next->prev = newNode;
    temp->next = newNode;
}
void deleteBeginning() {
    if (head == NULL) {
    printf("List is empty\n");
    return;
}
    struct Node* temp = head;
    head = head->next;
    if (head != NULL)
    head->prev = NULL;
    free(temp);
}
void deleteEnd() {
    if (head == NULL) {
    printf("List is empty\n");
    return;
}
    struct Node* temp = head;
    while (temp->next != NULL)
    temp = temp->next;
    if (temp->prev != NULL)
    temp->prev->next = NULL;
    else
    head = NULL;
    free(temp);
}
void deleteValue(int value) {
    struct Node* temp = head;
    while (temp != NULL && temp->data != value)
    temp = temp->next;
    if (temp == NULL) {
    printf("Value not found\n");
    return;
    }
    if (temp->prev != NULL)
    temp->prev->next = temp->next;
    else
    head = temp->next;
    if (temp->next != NULL)
    temp->next->prev = temp->prev;
    free(temp);
}
void displayForward() {
    struct Node* temp = head;
    printf("List (Forward): ");
    while (temp != NULL) {
    printf("%d <-> ", temp->data);
    temp = temp->next;
    }
    printf("NULL\n");
}
void displayBackward() {
    struct Node* temp = head;
    if (temp == NULL) return;

    while (temp->next != NULL)
    temp = temp->next;

    printf("List (Backward): ");
    while (temp != NULL) {
    printf("%d <-> ", temp->data);
    temp = temp->prev;
}
    printf("NULL\n");
}
int main() {
    int choice, data, pos;
    while (1) {
    printf("\n--- Doubly Linked List Menu ---\n");
    printf("1. Insert at Beginning\n");
    printf("2. Insert at End\n");
    printf("3. Insert at Position\n");
    printf("4. Delete from Beginning\n");
    printf("5. Delete from End\n");
    printf("6. Delete by Value\n");
    printf("7. Display Forward\n");
    printf("8. Display Backward\n");
    printf("9. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    switch (choice) {
    case 1:
        printf("Enter value: ");
        scanf("%d", &data);
        insertBeginning(data);
        break;
    case 2:
        printf("Enter value: ");
        scanf("%d", &data);
        insertEnd(data);
        break;
    case 3:
        printf("Enter value and position: ");
        scanf("%d%d", &data, &pos);
        insertAtPosition(data, pos);
        break;
    case 4:
        deleteBeginning();
        break;
    case 5:
        deleteEnd();
        break;
    case 6:
        printf("Enter value to delete: ");
        scanf("%d", &data);
        deleteValue(data);
        break;
    case 7:
        displayForward();
        break;
    case 8:
        displayBackward();
        break;
    case 9:
        exit(0);
    default:
    printf("Invalid choice\n");
}
}
}
