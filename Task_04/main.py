# Create restaurant
from Restaurant import Restaurant
from Menu import Menu
from Order import Order
from OrderItem import OrderItem
from MenuItem import MenuItem

# Create restaurant
restaurant = Restaurant("Tasty Bites", 0.08)

# Create menu items
burger =  MenuItem("M001", "Classic Burger",
    "Beef patty with lettuce, tomato, cheese", 12.99, "Main Course")
fries = MenuItem("M002", "French Fries",
    "Crispy golden fries", 4.99, "Appetizer")
salad =  MenuItem("M003", "Caesar Salad",
    "Fresh romaine with caesar dressing", 8.99, "Appetizer")
soda =  MenuItem("M004", "Soft Drink",
    "Coca-Cola, Sprite, or Fanta", 2.99, "Beverage")
cake =  MenuItem("M005", "Chocolate Cake",
    "Rich chocolate layer cake", 6.99, "Dessert")


# Add items to menu
restaurant.menu.addMenuItem(burger)
restaurant.menu.addMenuItem(fries)
restaurant.menu.addMenuItem(salad)
restaurant.menu.addMenuItem(soda)
restaurant.menu.addMenuItem(cake)

# # Display menu
# restaurant.menu.displayMenu()
# print('*' * 50)
# print()
# print()

########### Menu Class ############
# restaurant.menu.removeMenuItem('M001')
# restaurant.menu.displayMenu()
# print(restaurant.menu.getItemsByCategory('Appetizer'))
# print(restaurant.menu.searchItem('op'))

# # Create order for table 5
order1 = restaurant.createOrder(5)
order1.addItem(burger, 3, "No onions")
order1.addItem(fries, 1, "Extra crispy")
order1.addItem(soda, 2, "No ice")

print(restaurant.getPopularItems(1))

# # Display order summary
# print(order1.getOrderSummary())
# order1.removeItem('OI001')
# print(order1.getOrderSummary())


# # Calculate with tip
# subtotal = order1.getSubTotal()
# tax = order1.getTax(restaurant.taxRate)
# tip = order1.calculateTip(0.15)  # 15% tip
# total = order1.getTotal(restaurant.taxRate) + tip

# print(f"\nSubtotal: ${subtotal:.2f}")
# print(f"Tax (8%): ${tax:.2f}")
# print(f"Tip (15%): ${tip:.2f}")
# print(f"Total: ${total:.2f}")

# # # Update order status
# print("\nOrder status: " + order1.status)
# order1.updateStatus("Preparing")
# print("\nOrder status: " + order1.status)
# order1.updateStatus("Ready")
# print("Order status: " + order1.status)

# # # Complete order
# restaurant.completeOrder(order1.orderId)
# print("Order status: " + order1.status)

# # # Get revenue
# print("\nTotal Revenue: $" + str(restaurant.getTotalRevenue()))