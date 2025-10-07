pet_0 = {'animal': 'snake', 'owner': 'jamari'}
pet_1 = {'animal': 'dog', 'owner': 'Quincy'}
pet_2 = {'animal': 'Iguana', 'owner': 'Ariana'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['animal']}.")
