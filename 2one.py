#3. TUPLE = () ordered and unchangeable. Duplicates OK. FASTER

cars = ("BMW", "FERRARI", "FORD", "TOYOTA", "AUDI")

#print(dir(cars))
#print(help(cars))
print(len(cars))
print("bmw" in cars)       #like .contains()
print(cars.index("AUDI"))
cars.count("FORD")


print(cars)