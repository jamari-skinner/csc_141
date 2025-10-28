def describe_city(city, country='united states'):
    """Describe a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('new york')
#The city that never sleeps.
describe_city('paris', 'france')
#The city of love.
describe_city('tokyo', 'japan')
#The city of the best colors and tattoos.