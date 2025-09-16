guests = ['Morgan Freeman', 'Micheal Jordan', 'Drake', 'Angelina Jolie', 'Brad Pitt', 'Tiffany Haddish', 'Andrew Garfield']

print("Sorry everyone, the new table won’t arrive, so I can invite only two people.\n")

#Removde guests until only 2 remain

while len(guests) > 2: 
    removed_guest = guests.pop()
    print("Sorry " + removed_guest + ", I cant invite you to dinner.")

print("\nFinal invitations: ")
for guest in guests: 
    print("Dear " + guest + ", you're still invited!")

#Remove last two to make empty list
del guests[0]
del guests[0]

print("\nGuest list is now:", guests)