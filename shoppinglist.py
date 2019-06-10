def shoppingList():
    item_name = ""
    item_price = 0
    item_quantity = 0
    count = 0
    while(count <= 4):
      count += 1
      item_name = input("Please input shopping item name: ")
      item_price = float(input("Please input item price: "))
      item_quantity = int(input("Please input item quantity: "))

      print(f"Item Name: {item_name} Item Price: ${item_price} Item Quantity: {item_quantity}")


shoppingList()

'''total_item_price = item_price * item_price
print(f"Your total price is: ${total_item_price}")'''



 
   
    


