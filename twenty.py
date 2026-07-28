#2. SET = {} unordered and immutable, but Add/Remove is OK. NO duplicates

cars = {"BMW", "FERRARI", "FORD", "TOYOTA", "AUDI"}

#print(dir(cars))
#print(help(cars))
#print(len(cars))
#print("bmw" in cars)       #like .contains()
cars.add("SKODA")
cars.remove("FORD")
#cars.pop()
#cars.clear()

print(cars)