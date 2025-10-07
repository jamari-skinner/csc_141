fav_lango = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'lisa']

for person in people_to_poll:
    if person in fav_lango.keys():
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please partake in the poll!")