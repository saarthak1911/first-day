import pandas as pd

#a) Read the CSV
data = pd.read_csv("products.csv")

#b) Print each row in a clean format
print(data)

#c) Total number of rows
print("\nTotal number of rows:", len(data))

#d) Total number of products priced above 500
above_500 = data[data["price"] > 500]
print("\nProducts priced above 500:", len(above_500))

#e) Average price of all products
average_price = data["price"].mean()
print("\nAverage price of all products:", average_price)

#f) List all products belonging to a specific category (user input)
category = input("\nEnter category name: ")
filtered = data[data["category"].str.lower() == category.lower()]
print("\nProducts in category", category, ":")
print(filtered)

#g) Total quantity of all items in stock
total_qty = data["quantity"].sum()
print("\nTotal quantity of all items in stock:", total_qty)