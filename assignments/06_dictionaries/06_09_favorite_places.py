favorite_places = {
    'jamari': ['tokyo', 'los angeles', 'vermont'],
    'sarah': ['netherlands', 'rome'],
    'mike': ['gravity falls', 'seattle'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")
