def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"
#Home of Scott Pilgrim
pair = city_country('toronto', 'canada')
print(pair)
