#2D LISTS

#fruits     = ["apple", "orange", "banana", "coconut"]
#vegetables = ["spinach", "carrots", "potatoes"]
#meats      = ["chicken", "fish", "turkey"]

groceries = [["apple", "orange", "banana", "coconut"],
             ["spinach", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

#print(groceries[2])

for grocery in groceries:
    for food in grocery:
        print(food,end=" ")
    print()
