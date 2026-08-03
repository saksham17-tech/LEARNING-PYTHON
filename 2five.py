# dictionary = A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickl

capitals = {"USA": "Washington DC",
"India": "New Delhi",
"China": "Beijing",
"Russia" : "Moscow"}

capitals.update({"Germany" :"Berlin"})
capitals.update({"USA" :"Las Vegas"})
capitals.pop("China")
#capitals.clear()

print(capitals)
#print(capitals.get("Germany"))