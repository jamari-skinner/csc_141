guests = ["Juice WRLD", 'Drake', 'Brad Pitt', 'Tiffany Haddish']

for guest in guests: 
    print(f"Dear " + guest + ", I would love for you to join me for dinner.")

print("\nUnfortunately, " + guests[0] + " cant make it to dinner.\n")

#Remove by index
del guests[0]
#Replace Guest
guests.insert(0, "Micheal Jordan")

for guest in guests:
    print(f"Dear " + guest + ", I would love for you to join me for dinner.")