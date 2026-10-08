def q26_electricity_bill(units):
    if units <= 100:
        amount = units * 5
    elif units <= 200:
        amount = 500 + (units - 100) * 7
    else:
        amount = 1200 + (units - 200) * 10

    fixed = 100
    subtotal = amount + fixed
    tax = subtotal * 0.05
    discount = subtotal * 0.10 if units < 100 else 0

    return subtotal + tax - discount

def q27_consultation(charge):
    return charge

def q27_laboratory(charge):
    return charge

def q27_medicine(charge):
    return charge

def q27_room(charge):
    return charge

def q27_final_bill(consultation, laboratory, medicine, room, category):
    total = q27_consultation(consultation) + q27_laboratory(laboratory) + q27_medicine(medicine) + q27_room(room)

    if category == "senior":
        total *= 0.90
    elif category == "child":
        total *= 0.95

    return total

products = {}

def q28_add_product(name, price, quantity):
    products[name] = [price, quantity]

def q28_remove_product(name):
    if name in products:
        del products[name]

def q28_subtotal():
    return sum(price * quantity for price, quantity in products.values())

def q28_coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    return 0

def q28_gst(amount):
    return amount * 0.18

def q28_invoice(coupon):
    sub = q28_subtotal()
    discount = q28_coupon_discount(sub, coupon)
    tax = q28_gst(sub - discount)
    final = sub - discount + tax
    return sub, discount, tax, final

if __name__ == "__main__":
    print(q26_electricity_bill(250))

    print(q27_final_bill(500, 1000, 800, 2000, "senior"))

    q28_add_product("Laptop", 50000, 1)
    q28_add_product("Mouse", 1000, 2)
    print(q28_invoice("SAVE10"))
