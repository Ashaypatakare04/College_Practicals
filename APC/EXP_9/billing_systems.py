def electricity_bill(units):
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

def consultation(charge):
    return charge

def laboratory(charge):
    return charge

def medicine(charge):
    return charge

def room(charge):
    return charge

def hospital_bill(consultation_charge, laboratory_charge, medicine_charge, room_charge, category):
    total = consultation(consultation_charge) + laboratory(laboratory_charge) + medicine(medicine_charge) + room(room_charge)

    if category == "senior":
        total *= 0.90
    elif category == "child":
        total *= 0.95

    return total

products = {}

def add_product(name, price, quantity):
    products[name] = [price, quantity]

def remove_product(name):
    if name in products:
        del products[name]

def subtotal():
    return sum(price * quantity for price, quantity in products.values())

def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    return 0

def gst(amount):
    return amount * 0.18

def invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    tax = gst(sub - discount)
    return sub, discount, tax, sub - discount + tax

print("Electricity Bill:", electricity_bill(250))
print("Hospital Bill:", hospital_bill(500, 1000, 800, 2000, "senior"))

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
print("Shopping Invoice:", invoice("SAVE10"))
