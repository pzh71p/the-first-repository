cities = {
	'wuhan' : {
	'country' : 'china',
	'population' : '1232651.8',
	'fact' : 'jianghan_plain'
	},

	'chongqing' : {
	'country' : 'china',
	'population' : '3205420',
	'fact' : 'upper_reaches_of_the_Yangtze_River'
	},

	'new_york_city' : {
	'country' : 'america',
	'population' : '862000',
	'fact' : 'todd_mountain'
	}
} 

for city_name, city_info in cities.items():
	print(f"Information about {city_name.title()}:")
	print(f"\tCountry about {city_name.title()}:")
	print(f"\t{city_info['country'].title()}")
	print(f"\tPopulation about {city_name.title()}:")
	print(f"\t{city_info['population'].title()} Thousand")
	print(f"\tFact about {city_name.title()}:")
	print(f"\t{city_info['fact'].title()}\n")
	