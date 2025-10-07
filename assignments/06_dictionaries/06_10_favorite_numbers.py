favorite_numbers = {
    'jamari': [8, 23],
    'spongebob': [23, 44],
    'mike': [37, 16, 17],
    'juice': [999],
    'skrilla': [6, 7],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")
