#SHOPPING CART PROGRAM

item = str(input("\nWhat would you like to buy?  "))
price = float(input(f"What is the price of a {item}?  "))
qnt = int(input(f"How many {item} do you want?  "))

print(f"\nYou bought {qnt}x {item}(s).")
print(f"The total price of your purchase is = ${qnt*price:.2f}.")
