#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;
void insertBegin(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = val;
    newNode->next = head;
    head = newNode;
}
void insertEnd(int val) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* temp = head;
    newNode->data = val;
    newNode->next = NULL;
    if (head == NULL) {
    head = newNode;
    return;
}
    while (temp->next != NULL) {
    temp = temp->next;
}
    temp->next = newNode;
}
void insertAtPos(int val, int pos) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* temp = head;
    int i;
    newNode->data = val;
    if (pos == 1) {
    newNode->next = head;
    head = newNode;
    return;
}
    for (i = 1; i < pos - 1 && temp != NULL; i++) {
    temp = temp->next;
}
    if (temp == NULL) {
    printf("Position not found!\n");
    return;
}
    newNode->next = temp->next;
    temp->next = newNode;
}
void deleteBegin() {
    if (head == NULL) {
    printf("List is empty!\n");
    return;
}
    struct Node* temp = head;
    head = head->next;
    free(temp);
}
void deleteEnd() {
    if (head == NULL) {
    printf("List is empty!\n");
    return;
}
    struct Node* temp = head;
    struct Node* prev = NULL;
    if (head->next == NULL) {
    free(head);
    head = NULL;
    return;
}
    while (temp->next != NULL) {
    prev = temp;
    temp = temp->next;
}
    prev->next = NULL;
    free(temp);
}
void deleteAtPos(int pos) {
    if (head == NULL) {
    printf("List is empty!\n");
    return;
}
    struct Node* temp = head;
    int i;
    if (pos == 1) {
    head = temp->next;
    free(temp);
    return;
}
    for (i = 1; i < pos && temp != NULL; i++) {
    temp = temp->next;
}
    if (temp == NULL) {
    printf("Position not found!\n");
    return;
}
    struct Node* prev = head;
    for (i = 1; i < pos - 1; i++) {
    prev = prev->next;
}
    prev->next = temp->next;
    free(temp);
}
void display() {
    struct Node* temp = head;

    if (temp == NULL) {
    printf("List is empty!\n");
    return;
}
    printf("Linked List: ");
    while (temp != NULL) {
    printf("%d -> ", temp->data);
    temp = temp->next;
}
    printf("NULL\n");
}
int main() {
    int choice, val, pos;
    while (1) {
        printf("\n--- MENU ---\n");
        printf("1. Insert at Beginning\n");
        printf("2. Insert at End\n");
        printf("3. Insert at Position\n");
        printf("4. Delete from Beginning\n");
        printf("5. Delete from End\n");
        printf("6. Delete from Position\n");
        printf("7. Display\n");
        printf("8. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
    switch (choice) {
    case 1:
        printf("Enter value: ");
        scanf("%d", &val);
        insertBegin(val);
        break;
    case 2:
        printf("Enter value: ");
        scanf("%d", &val);
        insertEnd(val);
        break;
    case 3:
        printf("Enter value and position: ");
        scanf("%d %d", &val, &pos);
        insertAtPos(val, pos);
        break;
    case 4:
        deleteBegin();
        break;
    case 5:
        deleteEnd();
        break;
    case 6:
        printf("Enter position: ");
        scanf("%d", &pos);
        deleteAtPos(pos);
        break;
    case 7:
        display();
        break;
    case 8:
        exit(0);
    efault:
        printf("Invalid choice!\n");
}
}
    return 0;
}
