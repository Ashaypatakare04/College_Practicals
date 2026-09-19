inventory = {
    "Pen": 10,
    "Book": 20,
    "Bag": 5
}

product = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
inventory[product] = quantity

product = input("Enter product to update: ")
quantity = int(input("Enter new quantity: "))
inventory[product] = quantity

print("\nInventory:")
for product, quantity in inventory.items():
    print(product, ":", quantity)

highest = max(inventory, key=inventory.get)
print("Highest stock:", highest, inventory[highest])
