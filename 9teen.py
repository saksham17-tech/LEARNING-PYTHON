# collection = single "variable" used to store multiple values
#1. LIST = [] ordered and changeable. Duplicates OK

cars = ["BMW", "WOLKSWAGEN", "FERRARI", "FORD", "LAMBORGHINI"]

#print(cars[::-1])

#for car in cars:
#    print(car, end=" ")
#print()

#print(dir(cars))
#print(help(cars))

#print("BMW" in cars)    #like .contains()
cars.append("AUDI")
cars.insert(2, "MERCEDES")
#cars.sort()
#cars.reverse()
#cars.clear()
print(cars.index("FORD"))
print(cars.count("BMW"))

print(cars)