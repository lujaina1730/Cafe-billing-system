customer_name = input("Enter customer name: ")
item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price_per_item = float(input("Enter price_per_item (PKR): "))
subtotal = quantity * price_per_item
discount = subtotal * 0.05
final_amount = subtotal - discount
print("Customer name: ", customer_name)
print("Item name: ", item_name)
print("Quantity: ", quantity)
print("Price per item: ", price_per_item, "PKR")
print("Subtotal: ", subtotal,"PKR")
print("Discount: ", discount, "PKR")
print("Final amount: ", final_amount, "PKR")
print(type(customer_name))
print(type(item_name))
print(type(quantity))
print(type(price_per_item))
print(type(subtotal))
print(type(discount))
print(type(final_amount))

