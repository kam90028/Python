#Starting a coffee shop
#Let's build a robot barista!

print("Hello!  Welcome to Kevin's Koffee!")
name = input("What is your name? ")

# COFFEE MENU
menu = {"coffee": 4.50,
        "espresso": 3.00,
        "latte": 5.00,
        "cappuccino": 5.50,
        "americano": 3.50,
        "mocha": 5.25}

# EMPTY DICTIONARY FOR ITEMS ORDERED
my_order = {}

# COFFEE MENU DISPLAY
print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value: .2f}")
print("--------------------------")

print(f"Welcome, {name}!")
while True:
    order = input(f"Please select an item (q to quit)? ").lower()
    if order == "q":
        break 
    elif menu.get(order) is not None:
        quantity = int(input(f"How many {order}(s) would you like? "))
        my_order[order] = [quantity, (quantity * menu[order])]

# RECEIPT FOR ITEMS PURCHASED
print(f"Thank you, {name}! Here is your receipt: \n")
print("--------------------------")
print("          RECEIPT         ")
print("--------------------------")
for key, value in my_order.items():
    print(f"{value[0]} x {key:10}: ${value[1]:.2f}")
    print()
total = sum(item[1] for item in my_order.values())
print("--------------------------")
print(f"TOTAL         : ${total:.2f}")
print("--------------------------")
print("THANK YOU FOR COMING!!")