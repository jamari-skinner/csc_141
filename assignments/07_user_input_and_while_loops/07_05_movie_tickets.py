age = ""

while age != "quit":
    age = input("Enter your age (or 'quit' to stop): ")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    elif age <= 65:
        print("Your ticket is $5.")    
    else:
        print("Your ticket is $5.")