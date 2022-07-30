while True:
	pizza_input_toppings = input("Write a pizza topping or type quit to quit!")
	if pizza_input_toppings == 'quit':
		break
	else:
		print(f"We will append this topping : {pizza_input_toppings.title()}")