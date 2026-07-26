#string methods

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.find(" ") != -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")


msg = "obrigado"

print(f"\n{msg.rfind("o")}")
print(f"{msg.capitalize()}")
print(f"{msg.upper()}")
print(f"{msg.lower()}")
print(f"{msg.isdigit()}")
print(f"{msg.count("o")}")
print(f"{msg.replace("o","a")}")