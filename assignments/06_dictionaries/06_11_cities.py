# 6-11 Cities

cities = {
    'new_york': {
        'country': 'united states',
        'population': 8478000,
        'fact': 'It is known as the city that never sleeps.'
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'It has the busiest train station in the world.'
    },
    'paris': {
        'country': 'france',
        'population': 2050000,
        'fact': 'It is famous for the Eiffel Tower.'
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    country = info['country'].title()
    population = info['population']
    fact = info['fact']
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
