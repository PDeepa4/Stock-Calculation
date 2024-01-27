
# Creating a list called menu containing the items in cafe
menu = ['cakes', 'donuts', 'croissants', 'bagels', 'muffins']

# Creating a dictionary called stock for each item in menu
stock = {
    'cakes': 60, 
    'donuts': 50, 
    'croissants': 70, 
    'bagels':40, 
    'muffins': 35
    }

# Creating a dictionary called price for each item in menu
price = {
    'cakes': 4, 
    'donuts': 3, 
    'croissants': 2, 
    'bagels': 1, 
    'muffins': 2
    }

# Calculating the item value for each item on menu using 'for loop' (less comprehension)
item_value = {key: stock[key] * price[key] for key in stock and price}

# Calculating the total stock worth for all items in the cafe using 'for loop'.
# The loop iterates through each value in the item_value dictionary and adds them together.
total_stock = 0

for value in item_value.values():
    total_stock += value

# Printing out the result for ' the total_stock' of items in cafe.
print(f"The total stock worth in the cafe is: {total_stock}")