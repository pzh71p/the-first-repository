def get_formatted_name(first_name, last_name, middle=''):
	if middle:
		full_name = f"{first_name} {middle} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

#while True:
#	print("\nPlease tell me your name!")
#	print("Or hit 'q' to quit!")
#	first = input("Your first name?")
#	if first == 'q':
#		break
#middle = input("Your middle name?(If you did't have a middle name, hit [ENTER])")
#	last = input("Your las name?")
#	if last == 'q':
#		break
#	name = get_formatted_name(first, middle, last)
#	print(f"Your name is {name.title()}")


