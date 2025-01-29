menu = {"Pizza": {"Prize": 200,"description": "Cheese burst"},
"Coffee": {"price":45,"description":"Freshly brewed coffee"},
"Burger": {"price":80,"description":"Aloo Tiki Burger"},
"Pastry": {"price":55,"description":"Freshly bake blackforest cake"},
"Pasta": {"price":200,"description":"Italian pasta in red sauce"},
"Sandwich": {"price":70,"description":"Paneer tika sandwich"},
"Momos": {"price":60,"description":"Fried momos"},
}

orders = []

def view_menu():
  for item, details in menu.items():
    print(f"{item}: ${details['price']} - {details['description']}")

def take_order():
  order = {"customer": input("Enter customer name: "), "items": {}}
  while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == "done":
      break
    if item not in menu:
      print(f"Error: Item '{item}' not found on menu.")
      continue
    quantity = int(input(f"Enter quantity for {item}: "))
    order["items"][item] = quantity
  orders.append(order)
  print("Order added successfully!")

def calculate_bill(order):
  total_price = 0
  for item, quantity in order["items"].items():
    total_price += menu[item]["price"] * quantity
  return total_price

# Example usage
view_menu()
take_order()
order = orders[-1]  # Access the latest order
print(f"Customer: {order['customer']}")
for item, quantity in order["items"].items():
  print(f"{item} x {quantity}")
total_price = calculate_bill(order)
print(f"Total: ${total_price}")