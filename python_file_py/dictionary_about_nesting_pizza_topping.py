pizza = {
	'crust' : 'thick',
	'toppings' : ['mushroom','eatrcheese'],
}

print(f"You orderd a {pizza['crust'].upper()} -crust pizza"
	'"with the following toppings: ')

for topping in pizza['toppings']:
	print("\t" + topping)