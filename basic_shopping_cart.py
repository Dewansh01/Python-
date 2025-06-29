# Basic Shopping Cart

cart = []

def add_item(name, price):
    cart.append({"name": name, "price": price})
    print(f"{name} added to cart.")

def view_cart():
    if not cart:
        print("Cart is empty.")
    else:
        print("\nItems in Cart:")
        for item in cart:
            print(f"- {item['name']}: ₹{item['price']}")

def total_amount():
    total = sum(item['price'] for item in cart)
    print(f"\nTotal Amount: ₹{total}")

# Sample usage
add_item("Apple", 20)
add_item("Milk", 50)
view_cart()
total_amount()


#Output

# Apple added to cart.
# Milk added to cart.

# Items in Cart:
# - Apple: ₹20
# - Milk: ₹50

# Total Amount: ₹70
