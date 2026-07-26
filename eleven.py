#LOGICAL OPERATORS

#OR
temp = 25
is_raining = False
if temp>35 or temp<0 or is_raining:
    print("Outdoor event is cancelled.")
else:
    print("Outdoor event is still scheduled.")


#AND
temp = 25
is_Sunny = False
if temp>=28 and is_Sunny:
    print("The weather is hot and sunny.")
else:
    print("The weather is cool and cloudy.")


#NOT
is_Online = False
print(not is_Online)