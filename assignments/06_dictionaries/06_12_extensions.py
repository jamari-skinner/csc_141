
cities = {
    'new_york': {
        'country': 'united states',
        'population': 8478000,
        'fact': 'It is known as the city that never sleeps.',
        'landmark': 'Statue of Liberty'
    },
    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'It has the busiest train station in the world.',
        'landmark': 'Tokyo Tower'
    },

    'paris': {
        'country': 'france',
        'population': 2050000,
        'fact': 'It is famous for the Eiffel Tower.',
        'landmark': 'Eiffel Tower'
    },
    'sydney': {
        'country': 'australia',
        'population': 5000000,
        'fact': 'It is home to the Sydney Opera House.',
        'landmark': 'Sydney Harbour Bridge'
    },
}    

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")
    print(f"\tLandmark: {info['landmark']}")