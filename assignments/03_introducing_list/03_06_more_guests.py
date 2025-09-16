guests = ['Micheal Jordan', 'Drake', 'Brad Pitt', 'Tiffany Haddish']

print("Good News! I found a bigger table!\n")

#Add to beginning, middle and End
guests.insert(0, "Morgan Freeman")
guests.insert(3, "Angelina Jolie")
guests.append("Andrew Garfield")

for guest in guests:
    print("Dear " + guest + ", I would love for you to join me for dinner.")
