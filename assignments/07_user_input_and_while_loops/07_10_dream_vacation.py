responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    responses[name] = vacation

    repeat = input("Would you like to let someone else respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")