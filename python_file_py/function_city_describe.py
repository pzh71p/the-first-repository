def city_country(city, country, population=''):
	if population:
		message = f"{city.title()}, {country.title()} ---population {population}."
	else:
		message = f"{city.title()} belonged to {country.title()}."
	return message
