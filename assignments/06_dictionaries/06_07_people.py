person_0 = {'first_name': 'jamari', 'last_name': 'skinner', 'city': 'Capitol Heights'}
person_1 = {'first_name': 'jeremiah', 'last_name': 'parker', 'city': 'Landover'}
person_2 = {'first_name': 'joshua', 'last_name': 'harper', 'city': 'Bowie'}

people = [person_0, person_1, person_2]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    city = person['city'].title()
    print(f"{full_name} lives in {city}.")
