#using a while
prompt = "\nEnter a pizza topping (or 'quit' to stop): "
topping = input(prompt)
while topping != 'quit':
    print(f"I'll add {topping} to your pizza.")
    topping = input(prompt)

active = True
#Using a flag
while active:
    topping = input("\nEnter a pizza topping (or 'quit' to stop): ")
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
#USing break
while True:
    topping = input("\nEnter a pizza topping (or 'quit' to stop): ")

    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
